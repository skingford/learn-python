import ast
import re

import requests


def get_nodes_json():
    left_menu_text = requests.get("https://bbs.csdn.net/dynamic_js/left_menu.js?csdn").text
    nodes_str_match = re.search("forumNodes:(.*])", left_menu_text)
    if nodes_str_match:
        nodes_str = nodes_str_match.group(1).replace("null", "None")
        nodes = ast.literal_eval(nodes_str)
        return nodes
    return []


url_list = []


def process_nodes_list(nodes):
    for item in nodes:
        if "url" in item:
            url_list.append(item["url"])
            if "children" in item:
                process_nodes_list(item["children"])


if __name__ == "__main__":
    nodes_list = get_nodes_json()
    process_nodes_list(nodes_list)
    print(url_list)
