import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def analyzer_menu():
    choice = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )

    keys_of_choice = {
        "0": option0,
        "1": option1,
        "2": option2,
        "3": option3,
        "4": option4,
        "5": option5,
    }
    try:
        keys_of_choice[choice]()
    except (KeyError, ValueError):
        print("Opção inválida", file=sys.stderr)


def option0():
    return get_tech_news(int(input("Digite quantas notícias serão buscadas:")))


def option1():
    return search_by_title(input("Digite o título:"))


def option2():
    return search_by_date(input("Digite a data no formato aaaa-mm-dd:"))


def option3():
    return search_by_category(input("Digite a categoria:"))


def option4():
    return top_5_categories()


def option5():
    return print("Encerrando script")
