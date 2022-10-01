import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column (String(50), nullable= False)
    gender = Column (String(10), nullable= False)
    height = Column(Integer, primary_key=True)
    skin_color = Column (String(20), nullable= False)
    eye_color = Column (String(20), nullable= False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column (String(50), nullable= False)
    polulation = Column (Integer, primary_key=True)
    orbital_period = Column(Integer, primary_key=True)
    rotation_perio = Column(Integer, primary_key=True)
    diameter = Column(Integer, primary_key=True)

class FavoritoCharacter(Base):
    __tablename__ = 'favoritoCharacter'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    usuario = relationship(Usuario)
    character = relationship(Character)

class FavoritoPlanet(Base):
    __tablename__ = 'favoritoPlanet'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planer_id = Column(Integer, ForeignKey('planet.id'))
    usuario = relationship(Usuario)
    planet = relationship(Planet)
        
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')