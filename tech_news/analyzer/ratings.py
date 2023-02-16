from tech_news.database import find_news


def top_5_categories():
    list_of_news = find_news()
    count_category = dict()

    for new in list_of_news:
        if new["category"] in count_category.keys():
            count_category[new["category"]] += 1
        else:
            count_category[new["category"]] = 1

    list_of_categories = [
        ({"category": category, "amount": count_category[category]})
        for category in count_category
    ]

    list_of_categories.sort(
        key=lambda item: (-item["amount"], item["category"])
    )
    top5_categories = [
        category["category"] for category in list_of_categories[:5]
    ]

    return top5_categories
