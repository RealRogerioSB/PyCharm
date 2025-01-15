import redis
from sqlalchemy import create_engine, Column, Integer, String, Sequence, StaticPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url_redis = ("redis://default:oTAaMxsndx5SUHmKVZbTcT5uuhut3pss@redis-11006.c250.eu-central-1-1.ec2.redns.redis-cloud.co"
             "m:11006/0")

engine = create_engine(url_redis, poolclass=StaticPool)

# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     name = Column(String(50))
#     age = Column(Integer)


# engine = create_engine(url_redis)
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# Adicionando um usuário ao banco de dados SQL
# new_user = User(name='Jon Doe', age=28)
# session.add(new_user)
# session.commit()

# Configuração do Redis
# r = redis.Redis(host='redis-11006.c250.eu-central-1-1.ec2.redns.redis-cloud.com', port=11006, db=0)

# Adicionando uma chave-valor ao Redis
# r.set('user', 'Jon Doe')

# Recuperando o valor do Redis
# user = r.get('user')
# print(user.decode('utf-8'))
