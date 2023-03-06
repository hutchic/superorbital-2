# -*- coding: utf-8 -*-
import fire
from drone_cli import DroneCLI


def test_list_drone(capsys):
    fire.Fire(DroneCLI, ["list"])
    captured = capsys.readouterr()
    assert captured.out is not None
