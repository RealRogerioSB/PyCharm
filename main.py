from datetime import date

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app: FastAPI = FastAPI()

fake_db: list[dict[str: bool | date | int | str]] = [
    {"_id": 1, "_title": "Criando uma aplicação com Django", "_date": date.today(), "_published": True},
    {"_id": 2, "_title": "Criando uma aplicação com Flask", "_date": date.today(), "_published": True},
    {"_id": 3, "_title": "Criando uma aplicação com FastAPI", "_date": date.today(), "_published": False},
    {"_id": 4, "_title": "Criando uma aplicação com Starlette", "_date": date.today(), "_published": False},
]


class Post(BaseModel):
    _id: int
    title: str
    date: date = date.today()
    published: bool = True


@app.get("/post", tags=["Post"], status_code=status.HTTP_200_OK)
async def list_post() -> list:
    return fake_db


@app.get("/post/disponiveis", tags=["Post"], status_code=status.HTTP_200_OK)
async def list_post_disponiveis() -> list:
    return [fake for fake in fake_db if fake["_published"]]


@app.get("/post/{item}", tags=["Post"], status_code=status.HTTP_200_OK)
async def get_item_post(item: int) -> dict:
    for _item in fake_db:
        if _item["_id"] == item:
            return _item
    return {"mensagem": "Não foi possível localizar o item..."}


@app.post("/post", tags=["Post"], status_code=status.HTTP_201_CREATED)
async def create_post(fake: dict) -> dict:
    fake_db.append(fake)
    return {"mensagem": "Post criado com sucesso!"}


@app.put("/post/{item}", tags=["Post"], status_code=status.HTTP_200_OK)
async def update_post(item: int, _fake: dict) -> dict:
    for fake in fake_db:
        if fake["_id"] == item:
            fake["_title"] = _fake["_title"]
            fake["_date"] = _fake["_date"]
            fake["_published"] = _fake["_published"]
            return {"mensagem": "Post atualizado com sucesso!"}
    return {"mensagem": "Não foi possível localizar o item..."}


@app.delete("/post/{item}", tags=["Post"], status_code=status.HTTP_200_OK)
async def delete_post(item: int) -> dict:
    for index, _item in enumerate(fake_db):
        if _item["_id"] == item:
            fake_db.pop(index)
            return {"mensagem": "Post deletado com sucesso!"}
    return {"mensagem": "Não foi possível localizar o item..."}


if __name__ == '__main__':
    uvicorn.run(app="main:app", port=5000)
