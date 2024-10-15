from infra.configs.connection import DBConnectionHandler
from infra.entities.movies import Movies

class MoviesRepository:

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Movies).all()
            return data
        
    def insert(self,title, genre, year):
        with DBConnectionHandler() as db:
            data_insert = Movies(title=title, genre=genre,year=year)
            db.session.add(data_insert)
            db.session.commit()

    def deleteByTitle(self,title):
        with DBConnectionHandler() as db:
            db.session.query(Movies).filter(Movies.title == title).delete()
            db.session.commit()

    def updateYearByTitle(self, title, year):
        with DBConnectionHandler() as db:
           db.session.query(Movies).filter(Movies.title == title).update({"year": year})
           db.session.commit()