# -*- coding: utf-8 -*-
from json import JSONDecodeError
import fire
import pytest
from io import StringIO
from unittest.mock import Mock, patch
from drone_cli import DroneCLI
from swagger_client.rest import ApiException


class ApiClientContext:
    def __enter__(self):
        from swagger_client.api_client import ApiClient

        self.client = ApiClient()
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.client


# Test the list drone method
def test_list_drone(capsys):
    # Mock the API response
    mock_response = [{"id": 1, "name": "Drone 1"}, {"id": 2, "name": "Drone 2"}]
    with patch("swagger_client.DroneApi.list_drones", return_value=mock_response):
        # Call the list method
        fire.Fire(DroneCLI, ["list"])

    # Check that the output contains the names of the drones
    captured = capsys.readouterr()
    assert "Drone 1" in captured.out
    assert "Drone 2" in captured.out


# Test the create drone happy path
def test_create_drone_valid(capsys):
    with patch("swagger_client.DroneApi.create_drone") as mock_method:
        mock_response = {"id": 1, "name": "rubyred"}
        mock_method.return_value = mock_response
        fire.Fire(DroneCLI, ["create", "valid.json"])

    # Check that the output contains the name of the drone
    captured = capsys.readouterr()
    assert "rubyred" in captured.out

    # Check that the create_drone method was called once
    mock_method.assert_called_once()


# Test the create drone method with invalid filename
def test_create_drone_file_not_found(capsys):
    with pytest.raises(FileNotFoundError) as e:
        fire.Fire(DroneCLI, ["create", "not-found.json"])

    assert "No such file or directory" in str(e.value)


# Test the create drone method with invalid JSON
def test_create_drone_invalid_json(capsys):
    with pytest.raises(JSONDecodeError) as e:
        fire.Fire(DroneCLI, ["create", "invalid-json.json"])

    assert "Expecting value: line 1 column 1 (char 0)" in str(e.value)


# Test the create drone method with invalid plan
def test_create_drone_invalid_plan(capsys):
    with patch(
        "swagger_client.DroneApi.create_drone",
        side_effect=ApiException(status=400, reason="Bad Request"),
    ):
        with pytest.raises(ApiException) as e:
            with ApiClientContext():  # This isn't working and I'm not sure why
                fire.Fire(DroneCLI, ["create", "invalid-plan.json"])

        assert 400 == e.value.status
        assert "Bad Request" in e.value.reason


# Test the create drone method with invalid type
def test_create_drone_invalid_type(capsys):
    with pytest.raises(ValueError) as e:
        fire.Fire(DroneCLI, ["create", "invalid-type.json"])
    assert (
        str(e.value)
        == "Invalid value for `type` (invalid), must be one of ['quadcopter-small', 'quadcopter-large', 'plane-small', 'single-rotor-large']"
    )
