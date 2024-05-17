
from src.configurations.static import xpaths, link_labels
from src.utils.constants import CODE_CONFIGURATION
import os
import json


DATA_JSON_NAME = "dynamic.json"
DATA_JSON_PATH = os.path.join(CODE_CONFIGURATION, DATA_JSON_NAME)


def read_json_file(path):
    data = {}
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                data = json.load(file)
    except Exception as e:
        print(e)
        print("No data found")
    return data


def write_json_file(path, data):
    with open(path, 'w') as file:
        json.dump(data, file)
    print('New configurations saved successfully')


def sync_static_configuration():
    print("Syncing static configurations...")
    current_dynamic_configurations = read_json_file(DATA_JSON_PATH)

    current_xpaths = current_dynamic_configurations.get("xpaths", {})
    current_link_labels = current_dynamic_configurations.get("link_labels", {})

    for key, value in xpaths.items():
        if key not in current_xpaths:
            current_xpaths[key] = value

    for key, value in link_labels.items():
        if key not in current_link_labels:
            current_link_labels[key] = value

    write_json_file(DATA_JSON_PATH, {
        "xpaths": current_xpaths,
        "link_labels": current_link_labels
    })
    print("Syncing complete")
