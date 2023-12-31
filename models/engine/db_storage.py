#!/usr/bin/python3
"""Module for new DBStorage class"""
from os import getenv
from sqlalchemy import create_engine, MetaData


class DBStorage:
    """Defines the new engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the storage"""
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        """query on the current database session"""
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.city import City
        from models.base_model import Base

        classes = [
            City,
            User,
            Amenity,
            Place,
            Review,
            State
        ]
        rows = []
        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in classes:
                rows += self.__session.query(cls).all()
        return {type(ob).__name__ + "." + ob.id: ob for ob in rows}

    def new(self, obj):
        """add objects to database"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the db"""
        from models.base_model import Base
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        from sqlalchemy.orm import sessionmaker, scoped_session

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        session_option = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
                )
        Session = scoped_session(session_option)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.close()

    def close(self):
        """Close session"""
        self.__session.close()
