import requests
from parsel import Selector
from requests.exceptions import ConnectionError, HTTPError
from time import sleep


def fetch(url):
    header = {"user-agent": "Fake user-agent"}
    sleep(1)
    try:
        response = requests.get(url, headers=header, timeout=3)
        response.raise_for_status()
    except (ConnectionError, HTTPError, requests.Timeout):
        return None
    return response.text


def scrape_updates(html_content):
    result = Selector(html_content)
    urls_list = []
    for url_path in result.css("a.cs-overlay-link"):
        tag = url_path.css("a::attr(href)").get()
        urls_list.append(tag)
    return urls_list


def scrape_next_page_link(html_content):
    result = Selector(html_content)
    return result.css("a.next::attr(href)").get()


def scrape_news(html_content):
    result = Selector(text=html_content)
    data_news = {
        "url": result.css("link[rel='canonical']::attr(href)").get(),
        "title": result.css("h1.entry-title::text").get().strip(),
        "timestamp": result.css(".meta-date::text").get(),
        "writer": result.css(".author > a::text").get(),
        "reading_time": int(
            result.css(".meta-reading-time::text").re_first(r"\d*")
        ),
        "summary": result.xpath("string(//p)").get().strip(),
        "category": result.css(".label::text").get(),
    }

    return data_news


# {
#   "url": "https://blog.betrybe.com/novidades/noticia-bacana",
#   "title": "Notícia bacana",
#   "timestamp": "04/04/2021",
#   "writer": "Eu",
#   "reading_time": 4,
#   "summary": "Algo muito bacana aconteceu",
#   "category": "Ferramentas",
# }

# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


print(
    scrape_news(
        fetch(
            "https://blog.betrybe.com/tecnologia/sistema-operacional-windows/"
        )
    )
)
