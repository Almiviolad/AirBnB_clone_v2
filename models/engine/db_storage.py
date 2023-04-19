#!/usr/bin/python3
"""Defines dbstorage class"""


class DBStorage():
    __engine = None
    __session = None
    def __init__(self):
        """init an object"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """query object from.db"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        objs = self.__session.query(cls).fetchall()
        if cls is None:
            objs = self.__session.query()
        return (
