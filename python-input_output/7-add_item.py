#!/usr/bin/python3

"""Adds all arguments to a list and saves them to a file."""

from sys import argv

load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = load_file("add_item.json")
except (ValueError, FileNotFoundError):
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_file(json_list, "add_item.json")
