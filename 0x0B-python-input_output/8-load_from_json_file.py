#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, mode='r', encoding="utf-8") as myfile:
        return (json.load(myfile))
