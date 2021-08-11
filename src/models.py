import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(Integer, nullable=False)
    favorites_id = Column(Integer, ForeignKey("favorites.id"))
    favorites_set = relationship("Favorites", back_populates="parent", uselist=False)


class Favorites(Base):

    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planets_post = Column(Integer)
    starships_post = Column(Integer)
    people_post = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    user_set = relationship("User")


class Planets(Base):

    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    diameter = Column(String)
    films = Column(String)
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)
    residents = Column(String)
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String)
    url = Column(String)
    favorites_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship(Favorites)


class People(Base):

    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(String)
    eye_color = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    heigth = Column(Integer)
    homeworld = Column(String)
    mass = Column(Integer)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)
    url = Column(String)
    favorites_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship(Favorites)


class Starships(Base):

    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    MGT = Column(String)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    cost_in_credits = Column(Integer)
    created = Column(Integer)
    crew = Column(Integer)
    hyperdrive_rating = Column(Float)
    lenght = Column(Integer)
    manufacturer = Column(String)
    max_atmosphering_speed = Column(String)
    model = Column(String)
    passengers = Column(Integer)
    pilot = Column(String)
    starship_class = Column(String)
    url = Column(String)
    favorites_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship(Favorites)


def to_dict(self):
    return {}


render_er(Base, 'diagram.png')
