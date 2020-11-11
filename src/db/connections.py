from sqlalchemy import create_engine
from src.db.dtos import Base
from sqlalchemy.orm import sessionmaker

class DBOptions:
    def __init__(self, dbFile, echo):
        self.dbfile = dbFile
        self.echo = echo

class DBSession():
    def __init__(self, engine):
        self.session = sessionmaker(bind=engine)()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.commit()
        self.session.close()

    def query(self, queryClass):
        return self.session.query(queryClass)

    def add(self, item):
        self.session.add(item)

class DBManager():
    def __init__(self, options):
        self.engine = None
        self.options = options
        self.initialized = False
        
    def initialize(self):
        self.engine = create_engine(self.options.dbfile, echo=self.options.echo)
        Base.metadata.create_all(self.engine)
        self.initialized = True

    def connect(self):
        self._checkStatus()
        return DBConnection(self)

    def _checkStatus(self):
        if self.initialized == False:
            raise Exception("Cannot perform operations on DB before it's been initialized")

class DBConnection():
    def __init__(self, manager):
        self.session = None
        self.manager = manager

    def __enter__(self):
        self.session = DBSession(self.manager.engine)
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()