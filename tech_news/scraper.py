import requests
from requests.exceptions import ConnectionError, HTTPError
from time import sleep


def fetch(url):
    header = {"user-agent": "Fake user-agent"}
    sleep(1)
    try:
        response = requests.get(url, header, timeout=3)
        response.raise_for_status()
    except (ConnectionError, HTTPError, requests.Timeout):
        return None
    return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


print(fetch("https://app.betrybe.com/"))
