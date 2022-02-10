import ast
import re
from urllib import parse
from datetime import datetime

import requests
from scrapy import Selector

from models.csdn import Topic

domain = "https://bbs.csdn.net"
url_list = []


def get_nodes_json():
    left_menu_text = requests.get("https://bbs.csdn.net/dynamic_js/left_menu.js?csdn").text
    nodes_str_match = re.search("forumNodes:(.*])", left_menu_text)
    if nodes_str_match:
        nodes_str = nodes_str_match.group(1).replace("null", "None")
        nodes = ast.literal_eval(nodes_str)
        return nodes
    return []


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
    all_urls = []

    for url in url_list:
        if url not in level1_list:
            full_url = parse.urljoin(domain, url)
            last_urls.append(full_url)

    for url in last_urls:
        all_urls.append(url)
        all_urls.append(url + "/recommend")
        all_urls.append(url + "/closed")

    return all_urls


def parse_topic(url):
    pass


def parse_author(url):
    pass


def parse_list(url):
    res_text = requests.get(url).text
    sel = Selector(text=res_text)
    all_trs = sel.xpath("//table[@class='forums_tab_table']//tr")[2:]
    for tr in all_trs:
        status = tr.xpath("//td[1]/span/text()").extract()[0]
        score = tr.xpath("//td[2]/em/text()").extract()[0]
        topic_url = parse.urljoin(domain, tr.xpath("//td[3]/a/@href").extract()[0])
        topic_title = tr.xpath("//td[3]/a/text()").extract()[0]
        author_url = parse.urljoin(domain, tr.xpath("//td[4]/a/@href").extract()[0])
        author_id = author_url.split("/")[-1]
        create_time = tr.xpath("//td[4]/em/text()").extract()[0]
        answer_info = tr.xpath("//td[5]/span/text()").extract()[0]
        answer_nums = answer_info.split("/")[0]
        click_nums = answer_info.split("/")[1]
        last_time_str = tr.xpath("//td[6]/em/text()").extract()[0]
        last_time = datetime.strftime(last_time_str, "%Y-%m-%d %H:%M")

        topic = Topic()
        topic.status = status
        topic.score = score
        topic.id = int(topic_url.split("/")[-1])
        topic.title = topic_title
        topic.author = author_id
        topic.click_nums = click_nums
        topic.answer_nums = answer_nums
        topic.create_time = create_time
        topic.last_answer_time = last_time
        topic.save()

        parse_topic(topic_url)
        parse_author(author_url)

    next_page = sel.xpath("//a[@class='pagelistty_next_page']/@href").extract()
    if next_page:
        next_url = parse.urljoin(domain, next_page[0])
        parse_list(next_url)


if __name__ == "__main__":
    lst = get_last_urls()
    print(lst)
    print(len(lst))
