from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

produtos = [
    {
        "id": "1",
        "nome": "MacBook Pro M3 PRO",
        "descricao": "Um laptop fodástico",
        "preco": 13000.0,
        "disponivel": True
    },
    {
        "id": "2",
        "nome": "iPad Pro M1",
        "descricao": "Um tablet versátil",
        "preco": 8000.0,
        "disponivel": True
    },
    {
        "id": "3",
        "nome": "Mouse",
        "descricao": "Um periférico indispensável",
        "preco": 29.99,
        "disponivel": False
    },
]


class Produto(BaseModel):
    id: str
    nome: str
    descricao: Optional[str] = None
    preco: float
    disponivel: Optional[bool] = True


@app.get("/", tags=["root"])
async def root() -> dict:
    """Página Raíz"""
    return {"message": "Página Principal"}


@app.get("/produtos", tags=["produtos"])
async def listar_produtos() -> list:
    """Listar Produtos"""
    return produtos


@app.get("/produtos/disponiveis", tags=["produtos"])
async def listar_produtos_disponiveis() -> list:
    """Listar Produtos Disponíveis"""
    return [produto for produto in produtos if produto["disponivel"]]


@app.get("/produtos/{_id}", tags=["produtos"])
async def obter_produto(_id: str) -> dict:
    """Obter Produto"""
    for produto in produtos:
        if produto["id"] == _id:
            return produto
    return {}


@app.post("/novo_produto", tags=["produtos"])
def criar_produto(produto: Produto) -> dict:
    """Criar Novo Produto"""
    produtos.append(dict(produto))
    return {"mensagem": "Produto criado com sucesso!"}


@app.put("/produtos/{_id}", tags=["produtos"])
def atualizar_produto(_id: str, produto: Produto) -> dict:
    """Atualizar Produto"""
    for index, prod in enumerate(produtos):
        if prod["id"] == _id:
            produtos[index] = produto
            return {"mensagem": "Produto atualizado com sucesso!"}
    return {}


@app.delete("/produtos/{_id}", tags=["produtos"])
def excluir_produto(_id: str) -> dict:
    """Deletar Produto"""
    for index, prod in enumerate(produtos):
        if prod["id"] == _id:
            produtos.pop(index)
            return {"mensagem": "Produto removido com sucesso!"}
    return {}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
