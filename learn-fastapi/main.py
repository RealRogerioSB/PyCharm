from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

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


@app.get("/help")
def help():
    return {"mensagem": "Aprendendo ainda esse FastAPI..."}


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"mensagem": "Página Raíz"}


@app.get("/funci")
async def funci():
    return {
        "cd_usu_fun": "F8719981",
        "nm_usu_fun_abvd": "Rogério Balloussier",
    }


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
