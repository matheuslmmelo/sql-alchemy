from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


# Config
Base = declarative_base()
engine = create_engine("sqlite:///mydb.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Entities
class Movies(Base):
    __tablename__ = "movies"

    title = Column(String, primary_key=True)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Movie (title={self.title}, Year={self.year})"
    
Base.metadata.create_all(bind=engine)

#SQL

# Insert
insert_data = Movies(title="Batman", genre="Action", year=2020)
insert_data2 =  Movies(title="Man of Steel", genre="Action", year=2015)
insert_data3 =  Movies(title="Yes Sir", genre="Comedy", year=2010)
session.add(insert_data)
session.add(insert_data2)
session.add(insert_data3)
session.commit()

# Delete
session.query(Movies).filter(Movies.year == 2020).delete()
session.commit()

# Update
session.query(Movies).filter(Movies.genre == "Action").update({ "year": 2000})
session.commit()

# Select all
data = session.query(Movies).all()
print(data)

# Select one
data = session.query(Movies).filter(Movies.year>=2000).first()
print(data)

session.close()