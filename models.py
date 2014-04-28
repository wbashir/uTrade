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

# Set your classes here.

class Item(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    description = Column(String(140))

    def __init__(self, description=None):
        self.description = description


class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    description = Column(String(140))
    user_id = Column(Integer, ForeignKey('Users.id'))
    item_id = Column(Integer, ForeignKey('Items.id'))
    item = relationship(Item, backref=backref("item", uselist=False))

    def __init__(self, item=None, description=None,user_id=None):
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