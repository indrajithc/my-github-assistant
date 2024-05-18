
from src.configurations.static import xpaths, link_labels, ids
from src.utils.common_utils import read_json_file, write_json_file
from src.utils.constants import DATA_JSON_PATH


def sync_static_configuration():
    print("Syncing static configurations...")
    current_dynamic_configurations = read_json_file(DATA_JSON_PATH)

    current_xpaths = current_dynamic_configurations.get("xpaths", {})
    current_link_labels = current_dynamic_configurations.get("link_labels", {})
    current_ids = current_dynamic_configurations.get("ids", {})

    for key, value in xpaths.items():
        if key not in current_xpaths:
            current_xpaths[key] = value

    for key, value in link_labels.items():
        if key not in current_link_labels:
            current_link_labels[key] = value

    for key, value in ids.items():
        if key not in current_ids:
            current_ids[key] = value

    write_json_file(DATA_JSON_PATH, {
        "xpaths": current_xpaths,
        "link_labels": current_link_labels,
        "ids": current_ids
    })
    print("Syncing complete")
