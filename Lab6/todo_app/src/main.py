from fastapi import FastAPI, Body
import json
app = FastAPI()

@app.get("/api")
def api_get():
    return {"msg": "hello_world"}


@app.get("/books/{title}")
# curl 'http://127.0.0.1:8000/books/title'
# can add %20 to show space within the param str such as a%20b%20c
# param: str    specify the type of path_param
def api_get_path(title: str):
    return {"msg": title}


@app.get("/books/")
# curl 'http://127.0.0.1:8000/books/?title=The%20Sun%20Also%20Rises'
def api_get_query(title: str):
    return {"msg": title}


@app.get("/books/{title}/authors/")
# curl 'http://127.0.0.1:8000/books/The%20Sun%20Also%20Rises/authors/?author=ma'
def api_get_path_and_query(title: str, author: str | None = None):
    return {"msg": "title: " + title + ", author: " + author}


@app.post("/books/create_book")
# curl 'http://127.0.0.1:8000/books/create_book' -d '{"title": "An", "author": "Nassam talib", "category": "non-fiction"}'
# -X POST is optional, curl assumes a POST request when you provide data with the -d option.
# -d: requests with -d or have a body/data are considered post requests
def api_post(new_book=Body()):
    return {"msg": new_book}
    
    # Notes
    # return {"msg": new_book}
    # {"msg":"{\"title\": \"An\", \"author\": \"Nassam talib\", \"category\": \"non-fiction\"}"}
    
    # return {"msg": json.loads(new_book)}
    # {"msg":{"title":"An","author":"Nassam talib","category":"non-fiction"}}
    
    # bytes ==> new_book
    # dict ==> json.loads(new_book)
    
    # To check the data type of new_book(bytes)
    # 1.    data_type = type(new_book)
    #       return {"msg": f"new_book is of type {data_type}"}
    # 2. return {"msg": str(type(new_book))}


@app.put("/books/update_book/")
# curl -X PUT 'http://127.0.0.1:8000/books/update_book/?author=Ma' -d '{"title": "An", "author": "Nassam talib", "category": "non-fiction"}'
# for reference: https://fastapi.tiangolo.com/tutorial/body/
def api_put(new_book= Body(..., embed=True), author: str | None = None):
    new_book = json.loads(new_book)
    result = {**new_book, "author": author}
    # result = json.dumps(result, ensure_ascii=False)
    # return {"msg": new_book}
    return {"msg": result}


@app.delete("/books/{title}")
# curl -X DELETE 'http://127.0.0.1:8000/books/title'
def api_delete(title: str):
    return {"msg": f"Book {title} has been deleted."}