from dotenv import load_dotenv

import bs4
import os
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
import shutil
import subprocess
import sys
import time

load_dotenv()

__author__ = os.getenv('USER')
full_path = os.getenv('FULL_PATH')
user_agent = os.getenv('USER_AGENT')
headers = {'User-Agent':user_agent}


def get_web_content(url):
    try:
        res = requests.get(url, headers=headers, timeout=7, verify=False)
        time.sleep(5)
        if 'content-type' in res.headers:
            if res.status_code == 200 and 'text/html' in res.headers['content-type']:
                web_soup = bs4.BeautifulSoup(res.text, 'html.parser')
                return web_soup
            else:
                return False
        else:
            return False
    except Exception as e:
        return False

def judge_opendir(web_soup):
    if web_soup.title != None:
        if "Index of" in web_soup.title_string:
            return True
        else:
            return False
    else:
        return False

      
def get_opendir_parent(url):
    url_previos = url
    url_elem = url.split('/')
    base_url = f"{url_elem[0]}//{url_elem[2]}"
    for i in range(len(url_elem)-1, 2, -1):
        path = ''
        for j in range(3,i,1):
            path = f"{path}/{url_elem[j]}"
        web_soup = get_web_content(base_url + path)
        if web_soup != False:
            if judge_opendir(web_soup):
                url_previos = base_url + path
            else:
                return url_previos
        else:
            return url_previos
    return url_previos
  
def write_content(output_path, content):
    with open(output_path, content) as f:
        f.write(content)
        
        
def get_screenshot(url, output):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'--user-agent={user_agent}')
        chrome_service = service.Service(executable_path=full_path)
        driver = webdriver.Chrome(service=chrome_service, options=options)
        driver.set_page_load_timeout(10)
        driver.get(url)
        width = driver.execute_script('return document.body.scrollWidth')
        height = driver.execute_script('return document.body.scrollHeight')
        driver.set_window_size(int(width),int(height))
        driver.save_screenshot(output)
        driver.quit()
        time.sleep(5)
        return 1
    except Exception as e:
        print(e)
        return -1
