import abc
import barky


class AbstractRepository(abc.ABC):
    """
    Python's provisions for creating class hiearchy abstractions is provided in the module `abc`:
    https://docs.python.org/3.9/library/abc.html
    """

    @abc.abstractmethod
    def add(self, bookmark: barky.Bookmark):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> barky.Bookmark:
        raise NotImplementedError



class SqlAlchemyRepository(AbstractRepository):
    """
    A concrete SqlAlchemy implementation of the AbstractRepository 
    """

    def __init__(self, session):
        self.session = session

    def add(self, bookmark):
        self.session.add(bookmark)

    def get(self, title):
        return self.session.query(barky.Bookmark).filter_by(title=title).one()

    def list(self):
        return self.session.query(barky.Bookmark).all()