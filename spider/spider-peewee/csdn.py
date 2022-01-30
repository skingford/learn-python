import ast
import re

import requests
from urllib import parse

domain = "https://bbs.csdn.net"


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
        if "url" in item and item["url"]:
            url_list.append(item["url"])
            if "children" in item:
                process_nodes_list(item["children"])


def get_level1_list(nodes):
    level1_url = []
    for item in nodes:
        if "url" in item and item["url"]:
            level1_url.append(item["url"])
    return level1_url


def get_last_urls():
    nodes_list = get_nodes_json()
    process_nodes_list(nodes_list)
    level1_list = get_level1_list(nodes_list)
    last_urls = []
    for url in url_list:
        if url not in level1_list:
            full_url = parse.urljoin(domain, url)
            last_urls.append(full_url)

    all_urls = []
    for url in last_urls:
        all_urls.append(url)
        all_urls.append(url + "/recommend")
        all_urls.append(url + "/closed")
    return all_urls


if __name__ == "__main__":
    lst = get_last_urls()
    print(lst)
    print(len(lst))
