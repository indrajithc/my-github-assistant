from src.utils.constants import DATA_JSON_PATH
from src.utils.common_utils import read_json_file


def read_label(label_key):
    dynamic_configurations = read_json_file(DATA_JSON_PATH)
    return dynamic_configurations.get("link_labels", {}).get(label_key, None)


def read_xpath(xpath_key):
    dynamic_configurations = read_json_file(DATA_JSON_PATH)
    print(dynamic_configurations)
    xpath = dynamic_configurations.get("xpaths", {}).get(xpath_key, None)
    print(xpath)
    return xpath
