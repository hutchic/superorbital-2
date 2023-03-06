# -*- coding: utf-8 -*-
import fire
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


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
        pass

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
            print("Exception when calling DroneApi->list_drones: %s\n" % e)


if __name__ == "__main__":
    fire.Fire(DroneCLI())
