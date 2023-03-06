# -*- coding: utf-8 -*-
import fire
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


class DroneCLI:
    """
    a cli for interacting with the drones api
    """

    def __init__(self):
        configuration = swagger_client.Configuration()
        configuration.host = "http://localhost:8080"
        configuration.api_key["Authorization"] = "OMGSOSEKRET"
        self.api_client = swagger_client.ApiClient(configuration)

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
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling DroneApi->list_drones: %s\n" % e)


if __name__ == "__main__":
    fire.Fire(DroneCLI())
