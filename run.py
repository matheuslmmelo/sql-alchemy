from infra.repositories.movies_repository import MoviesRepository
from infra.configs.connection import DBConnectionHandler
from infra.configs.base import Base

with DBConnectionHandler() as db:
    Base.metadata.create_all(bind=db.get_engine())


repo = MoviesRepository()
repo.insert('someMovie','comedy',2010)
repo.insert('anotherMovie','comedy',2020)
repo.deleteByTitle('someMovie')

data = repo.select()
print(data)