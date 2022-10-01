from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

# an example mapping using the base
class Favoritos(Base):
    __tablename__ = 'favoritos'

    usuario_id = Column(Integer, primary_key=True)
    favorito_id = Column(String)
    