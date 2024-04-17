# _*_ coding: utf-8 _*_
"""
# Author: aidbdotsite
# Created Time : Thu Aug 24 17:17:50 2023

# File Name: main.py
# Description:

"""

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/favicon.ico")
def read_favicon():
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
