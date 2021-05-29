import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__= 'User'
    id_user = Column(Integer, primary_key=True)
    password = Column(String (32))
    name = Column(String (250))
    username = Column(String (250))

class Character (Base):
    __tablename__= 'Characters'
    id_character = Column(Integer, primary_key=True)
    name = Column(String (35))
    gender = Column(String (10))
    homeworld = Column(String (35))
    height = Column(Integer)
    species = Column(String (35))

class Planets (Base):
    __tablename__= 'Planets'
    id_planet = Column(Integer, primary_key=True)
    name = Column(String (35))
    climate = Column(String (10))
    diameter = Column(Integer)
    population = Column(Integer)
    terrain = Column(String (35))
 
class Favorites (Base):
    __tablename__= 'Favorites'
    id = Column(Integer, primary_key=True)
    id_fav_planets = Column(Integer, ForeignKey('planets.id_planet'))
    planets = relationship(Planets)
    id_fav_characters = Column(Integer, ForeignKey('characters.id_character'))
    character = relationship(Character)
    favorites = Column(Integer, ForeignKey('user.id_user'))
    user = relationship(User)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')