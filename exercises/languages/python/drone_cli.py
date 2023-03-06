# -*- coding: utf-8 -*-
import logging
import fire
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from urllib3.util.retry import Retry
import json


class DroneCLI:
    """
    a cli for interacting with the drones api
    """

    def __init__(self):
        # Create a custom Retry object with appropriate settings
        retry = Retry(
            total=5,  # Maximum number of retries to allow
            backoff_factor=1,  # Backoff factor for exponential backoff
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry on
        )

        configuration = swagger_client.Configuration()
        configuration.host = "http://localhost:8080"
        configuration.api_key["Authorization"] = "OMGSOSEKRET"
        self.api_client = swagger_client.ApiClient(configuration)
        self.api_client.rest_client.pool_manager.connection_pool_kw["retries"] = retry

    def create(self, filename):
        """
        creates a drone
        :param filename: filename containing json payload for creating drone
        :returns: drone created
        """
        logger = logging.getLogger(__name__)
        try:
            with open(filename, "r") as f:
                if not f:
                    raise Exception(f"Error: File {filename} is empty")
                payload = json.load(f)
        except FileNotFoundError:
            logger.error(f"Error: File {filename} not found")
            return None
        except json.decoder.JSONDecodeError as e:
            logger.error(f"Error: Invalid JSON file - {e}")
            return None

        """
        Assuming the default instruction index is 0. This should be handled by the API.
        """
        payload["instruction_index"] = 0

        drone = swagger_client.ModelsDrone(**payload)

        try:
            api_instance = swagger_client.DroneApi(self.api_client)
            api_response = api_instance.create_drone(drone)
            return pprint(api_response)
        except swagger_client.rest.ApiException as e:
            logger.error(f"Exception when calling DroneApi->create_drone: {e}")
            raise

    def list(self):
        """
        lists drones
        :returns list of drones
        """
        try:
            api_instance = swagger_client.DroneApi(self.api_client)
            api_response = api_instance.list_drones()
            return pprint(api_response)
        except ApiException as e:
            return print("Exception when calling DroneApi->list_drones: %s\n" % e)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    fire.Fire(DroneCLI())
