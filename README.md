# Tech News - Raspagem de dados

# Contexto
Este projeto tem como objetivo fazer uma raspagem de dados em um blog de notícias e reutiliza-lás.

## Técnologias usadas

Back-end:
> Desenvolvido usando: Python, Requests, Parsel , MongoDB, Pymongo

## Instalando Dependências

> Backend
```bash
Crie um ambiente virtual 
  python3 -m venv .venv && source .venv/bin/activate
  
  Instale as dependências
  python3 -m pip install -r dev-requirements.txt
``` 
## Executando aplicação

* Para rodar o back-end:

  ```
  1 - Para acessar o menu no terminal
    python3 tech_news/menu.py
  
  2 - Selecione 0 para popular o banco com notícias
  
    Selecione uma das opções a seguir:
    0 - Popular o banco com notícias;
    1 - Buscar notícias por título;
    2 - Buscar notícias por data;
    3 - Buscar notícias por categoria;
    4 - Listar top 5 categorias;
    5 - Sair.
 
   3 - Rode novamente para escolher como fará a sua busca 
     python3 tech_news/menu.py
 
  ```


https://user-images.githubusercontent.com/89083420/219815447-4fe5b3e5-d0a0-42db-b89c-f416416b91d5.mp4



