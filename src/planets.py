from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

# an example mapping using the base
class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    poblacion = Column(Integer, nullable=False)
    clima = Column(String)
    gravedad = Column(Integer, nullable=False)
    diametro = Column(String)

