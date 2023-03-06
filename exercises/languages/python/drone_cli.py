# -*- coding: utf-8 -*-
import fire


class DroneCLI:
    """
    a cli for interacting with the drones api
    """

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
        pass


if __name__ == "__main__":
    fire.Fire(DroneCLI())
