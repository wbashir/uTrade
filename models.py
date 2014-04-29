from flask import json
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('mysql://uTrade:F7!93pwu@localhost:8889/uTrade', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)


# Set your classes here.

class Item(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    description = Column(String(140))
    img_url = Column(String(200))

    def __init__(self, description=None, title=None, img_url=None):
        self.description = description
        self.title = title
        self.img_url = img_url

    @property
    def json(self):
        return to_json(self, self.__class__)


class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    description = Column(String(140))
    user_id = Column(Integer, ForeignKey('Users.id'))
    item_id = Column(Integer, ForeignKey('Items.id'))
    item = relationship(Item, backref=backref("item", uselist=False))

    def __init__(self, item=None, description=None, user_id=None):
        self.description = description
        self.item = item
        self.user_id = user_id


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    email = Column(String(120), unique=True)
    posts = relationship(Post, backref='author', lazy='dynamic')


    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email


# Create tables.
Base.metadata.create_all(bind=engine)