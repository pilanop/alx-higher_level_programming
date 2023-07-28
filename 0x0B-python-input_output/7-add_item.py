#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argument = sys.argv

if os.path.exists("add_item.json"):
    loaded = load_from_json_file("add_item.json")
    to_be = loaded + argument[1:]
    save_to_json_file(to_be, "add_item.json")
else:
    save_to_json_file(argument[1:], "add_item.json")
