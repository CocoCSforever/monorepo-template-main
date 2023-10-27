import requests
import json
from json.decoder import JSONDecodeError
from ..src import main

def test_api_get():
    target = main.api_get()
    assert target == {"msg": "hello_world"}


    # url = "http://127.0.0.1:8000/api"
    # response = requests.get(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": "hello_world"}


def test_api_get_path():
    title = "book_title test"
    target = main.api_get_path(title)
    assert target == {"msg": title}

    title = "second_title test"
    target = main.api_get_path(title)
    assert target == {"msg": title}


    # path_param = "book_title"
    # url = f"http://127.0.0.1:8000/books/{path_param}"
    # response = requests.get(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": path_param}

    # path_param = "second_test_title"
    # url = f"http://127.0.0.1:8000/books/{path_param}"
    # response = requests.get(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": path_param}


def test_api_get_query():
    title = "The Sun Also Rises"
    target = main.api_get_query(title)
    assert target == {"msg": title}

    title = "A Good Book"
    target = main.api_get_query(title)
    assert target == {"msg": title}


    # title = "The%20Sun%20Also%20Rises"
    # url = f"http://127.0.0.1:8000/books/?title={title}"
    # response = requests.get(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": title.replace("%20", " ")}

    # title = "A%20Good%20Book"
    # url = f"http://127.0.0.1:8000/books/?title={title}"
    # response = requests.get(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": title.replace("%20", " ")}

def test_api_get_path_and_query():
    title = "The Sun Also Rises"
    author = "Yijia Ma"
    target = main.api_get_path_and_query(title, author)
    assert target == {"msg": "title: " + title + ", author: " + author}

    title = "A Good Book"
    target = main.api_get_path_and_query(title, author)
    assert target == {"msg": "title: " + title + ", author: " + author}

    author = None
    target = main.api_get_path_and_query(title)
    assert target == {"msg": "title: " + title + ", author: " + str(author)}


    # title = "The%20Sun%20Also%20Rises"
    # author = "Yijia%20Ma"
    # url = f"http://127.0.0.1:8000/books/{title}/authors/?author={author}"
    # response = requests.get(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": "title: " + title.replace("%20", " ") + ", author: " + author.replace("%20", " ")}

    # title = "A%20Good%20Book"
    # author = "Yijia%20King"
    # url = f"http://127.0.0.1:8000/books/{title}/authors/?author={author}"
    # response = requests.get(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": "title: " + title.replace("%20", " ") + ", author: " + author.replace("%20", " ")}

def test_api_post():
    body = {"title": "The Sun Also Rises", "author": "Nassam Talib", "category": "non-fiction"}
    target = main.api_post(body)
    assert target == {"msg": body}

    body = {"title": "A Good Book", "author": "More Time", "category": "fiction"}
    target = main.api_post(body)
    assert target == {"msg": body}


    # url = "http://127.0.0.1:8000/books/create_book"
    # body = {"title": "The Sun Also Rises", "author": "Nassam Talib", "category": "non-fiction"}
    # response = requests.post(url, json=body)
    # assert response.status_code == 200
    
    # assert type(response.json()["msg"]) == type(body)
    # assert response.json()["msg"] == body

    # body = {"title": "A Good Book", "author": "More Time", "category": "fiction"}
    # response = requests.post(url, json=body)
    # assert response.status_code == 200
    # assert response.json()["msg"] == body

# checked with professor that it doesn't work for pytest but works using curl or postman
def test_api_put():
    body = {"title": "The Sun Also Rises", "author": "Nassam Talib", "category": "non-fiction"}
    author = "Yijia Ma"
    target = main.api_put(body, author)
    assert target == {"msg": {**body, "author": author}}

    body = {"title": "A Good Book", "author": "More Time", "category": "fiction"}
    target = main.api_put(body, author)
    assert target == {"msg": {**body, "author": author}}


    author = None
    target = main.api_put(body)
    assert target == {"msg": {**body, "author": author}}


    # author = "Yijia%20Ma"
    # url = f"http://127.0.0.1:8000/books/update_book/?author={author}"
    # body = {"title": "The Sun Also Rises", "author": "Nassam Talib", "category": "non-fiction"}
    # try:
    #     response = requests.put(url, json=body)
    #     response.raise_for_status()  # Check for HTTP errors
    #     data = response.json()
    # except JSONDecodeError as e:
    #     print(f"Error decoding JSON: {e}")
    # except requests.exceptions.RequestException as e:
    #     print(f"Request error: {e}")

    # -----------debug---------------------
    # body["author"] = author.replace("%20", " ")
    # print("sss")
    # print(body["author"])
    # print(body)
    # response = requests.put(url, json=body)
    # print(response.json())
    
    # print(response.text)
    # assert response.status_code == 200
    # assert response.json()["msg"] == body


def test_api_delete():
    title = "book_title test"
    target = main.api_delete(title)
    assert target == {"msg": f"Book {title} has been deleted."}

    title = "second_title test"
    target = main.api_delete(title)
    assert target == {"msg": f"Book {title} has been deleted."}


    # title = "book_title"
    # url = f"http://127.0.0.1:8000/books/{title}"
    # response = requests.delete(url)
    # assert response.status_code == 200
    # assert response.json() == {"msg": f"Book {title} has been deleted."}

    # title = "second%20title%20test"
    # url = f"http://127.0.0.1:8000/books/{title}"
    # response = requests.delete(url)
    # title = title.replace("%20", " ")
    # assert response.status_code == 200
    # assert response.json() == {"msg": f"Book {title} has been deleted."}