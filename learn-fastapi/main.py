import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host="redis-11006.c250.eu-central-1-1.ec2.redns.redis-cloud.com",
    port=11006,
    decode_responses=True,
    username="default",
    password="oTAaMxsndx5SUHmKVZbTcT5uuhut3pss",
)


class Product(HashModel):
    name: str
    price: float
    quantify: int

    class Meta:
        database = redis


@app.get("/")
def root():
    return {"mensagem": "Aprendendo o FastAPI!"}


@app.post("/products")
def create(product: Product):
    return product.save()


def redraw(pk: str):
    product = Product.get(pk)
    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantify": product.quantify,
    }


@app.get("/products")
def get():
    return [redraw(pk) for pk in Product.all_pks()]


@app.get("/products/{pk}")
def get_product(pk: str):
    return Product.get(pk)


if __name__ == "__main__":
    uvicorn.run("learn-fastapi.main:app", reload=True)