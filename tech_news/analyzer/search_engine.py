from tech_news.database import find_news


def search_by_title(title):
    list_of_news = find_news()
    select_news = [
        (new["title"], new["url"])
        for new in list_of_news
        if title.lower() in new["title"].lower()
    ]

    return select_news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
