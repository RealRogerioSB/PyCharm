from datetime import datetime, timedelta, UTC

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Post(BaseModel):
    _id: int
    _title: str
    _date: datetime = datetime.now(UTC)
    _published: bool = True


list_post = [
    {"_id": 1, "_title": "Aplicação de FastAPI", "_date": datetime.now(UTC), "_published": True},
    {"_id": 2, "_title": "Aplicação de Django", "_date": datetime.now(UTC) - timedelta(days=365), "_published": False},
    {"_id": 3, "_title": "Aplicação de Flask", "_date": datetime.now(UTC) - timedelta(weeks=9), "_published": True},
    {"_id": 4, "_title": "Aplicação de Starlette", "_date": datetime.now(UTC) - timedelta(hours=44), "_published": False},
]

app = FastAPI()


@app.get(path="/")
async def root() -> dict:
    return {"mensagem": "Página Raíz"}


@app.get(path="/posts")
async def listar_posts() -> list:
    return list_post


@app.get(path="/posts/disponiveis")
async def listar_disponiveis() -> list:
    return [post for post in list_post if post["_published"]]


@app.get(path="/posts/{item}")
async def obter_posts(item: int) -> dict:
    for post in list_post:
        if post["_id"] == item:
            return post
    return {"mensagem": "Não foi encontrado o item..."}


@app.post(path="/posts")
async def create_post(_new: dict) -> dict:
    list_post.append(_new)
    return {"mensagem": "Post criado com sucesso!"}


@app.put(path="/posts/{item}")
async def update_post(item: int, _post: dict) -> dict:
    for post in list_post:
        if post["_id"] == item:
            post["_title"] = _post["_title"]
            post["_published"] = _post["_published"]
            return {"mensagem": "Post atualizado com sucesso!"}
    return {"mensagem": "Não foi encontrado o item..."}


@app.delete(path="/posts/{item}")
async def delete_post(item: int) -> dict:
    for index, post in enumerate(list_post):
        if post["_id"] == item:
            list_post.pop(index)
            return {"mensagem": "Post removido com sucesso!"}
    return {"mensagem": "Não foi encontrado o item..."}


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=5000)
