from src.utils.constants import DATA_JSON_PATH
from src.utils.common_utils import read_json_file


def read_label(label_key):
    dynamic_configurations = read_json_file(DATA_JSON_PATH)
    return dynamic_configurations.get("link_labels", {}).get(label_key, None)


def read_xpath(xpath_key):
    dynamic_configurations = read_json_file(DATA_JSON_PATH)
    xpath = dynamic_configurations.get("xpaths", {}).get(xpath_key, None)
    return xpath


def read_id(id_key):
    dynamic_configurations = read_json_file(DATA_JSON_PATH)
    id = dynamic_configurations.get("ids", {}).get(id_key, None)
    return id
