from tech_news.database import find_news, search_news
from datetime import datetime


def search_by_title(title):
    list_of_news = find_news()
    select_news = [
        (new["title"], new["url"])
        for new in list_of_news
        if title.lower() in new["title"].lower()
    ]

    return select_news


def search_by_date(date):
    try:
        date_pattern = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        return [
            (new["title"], new["url"])
            for new in search_news({"timestamp": date_pattern})
        ]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
