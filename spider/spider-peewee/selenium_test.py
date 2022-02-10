import requests
import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://blog.csdn.net/")

time.sleep(5)
cookies = browser.get_cookies()
cookie_dict = {}
for item in cookies:
    cookie_dict[item["name"]] = item["value"]

print(requests.get("https://bbs.csdn.net/forums/openharmonyos", cookies=cookie_dict).text)
