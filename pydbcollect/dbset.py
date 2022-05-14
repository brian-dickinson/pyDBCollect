import base64
import os
import sqlite3
import string
import sys
from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.future import create_engine
from sqlalchemy import text, Column, Integer, String, BigInteger, PickleType, LargeBinary, delete, insert, exists, \
    literal
from sqlalchemy.orm import Session, declarative_base
from collections.abc import MutableSet, Set
from random import choice
from typing import Iterator, TypeVar, Iterable, Any
import uuid

from sqlalchemy.pool import StaticPool

_T = TypeVar('_T')
_T_co = TypeVar('_T_co', covariant=True)

Base = declarative_base()


def DBSet_Hash(obj):
    if isinstance(obj, str):
        b = obj.encode('UTF-8')
        return int.from_bytes(b, 'big') % sys.maxsize
    if isinstance(obj, bytes):
        return int.from_bytes(obj, 'big') % sys.maxsize
    if isinstance(obj, datetime):
        return ((obj - datetime(1, 1, 1)).total_seconds() * 1000) % sys.maxsize
    return hash(obj)


class DBSet_Meta(Base):
    __tablename__ = "META_SET_TABLE"
    __table_args__ = {'extend_existing': True}
    tablename = Column(String, primary_key=True)
    python_version = Column(String, nullable=True)
    packages = Column(String, nullable=True)

    def __init__(self, tablename):
        self.tablename = tablename

    @property
    def entry_class(self):
        if not hasattr(self, "_EntryClass"):
            class OutSet(Base):
                __tablename__ = self.tablename
                __table_args__ = {'extend_existing': True}
                element_id = Column(LargeBinary(32), primary_key=True)
                hash = Column(BigInteger)
                data = Column(PickleType, unique=True)

                def __init__(self, entry):
                    self.hash = DBSet_Hash(entry)
                    self.data = entry
                    self.element_id = uuid.uuid4().bytes

            self._EntryClass = OutSet
        return self._EntryClass


class DBSetIter():
    def __init__(self, seq, size):
        self.seq = seq
        self.size = size

    def __next__(self):
        return next(self.seq)

    def __length_hint__(self):
        return self.size


class DBSet(MutableSet):
    __slots__ = ('db_url', 'engine', 'name', 'session', 'db_table', '__weakref__')

    def __contains__(self, x: object) -> bool:
        # for entry in self.session.query(self.db_table.entry_class).where(
        #         self.db_table.entry_class.hash == DBSet_Hash(x)).all():
        #     if entry.data == x:
        #         return True
        # return False
        DBSet_Hash(x)
        x == 0
        return self.session.query(literal(True)).filter(exists().where(self.db_table.entry_class.hash == DBSet_Hash(x)).
                                                        where(self.db_table.entry_class.data == x)).limit(1).scalar()

    def __len__(self) -> int:
        return self.session.query(self.db_table.entry_class).count()

    def __iter__(self) -> Iterator[_T_co]:
        entries = self.session.query(self.db_table.entry_class).all()
        it = (x.data for x in entries)
        return DBSetIter(it, len(self))
        # for obj in entries:
        #     yield obj.data

    def discard(self, value: _T) -> None:
        for entry in self.session.query(self.db_table.entry_class).where(
                self.db_table.entry_class.hash == DBSet_Hash(value)).all():
            if entry.data == value:
                self.session.execute(
                    delete(self.db_table.entry_class).where(self.db_table.entry_class.element_id == entry.element_id))
                self.session.commit()
                return None

    def __init__(self, iter: Iterator = [], **kwargs):
        if "db_url" in kwargs:
            self.db_url = kwargs["db_url"]
            self.engine = create_engine(self.db_url, echo=False, future=True)
        else:
            self.db_url = "sqlite:///:memory:?blank"
            DB_URI = 'file::memory:?cache=shared'
            PY2 = sys.version_info.major == 2
            if PY2:
                params = {}
            else:
                params = {'uri': True}

            creator = lambda: sqlite3.connect(DB_URI, **params)
            self.engine = create_engine(self.db_url, echo=False, future=True,
                                        creator=creator)

        Base.metadata.create_all(self.engine)
        self.name = base64.urlsafe_b64encode(os.urandom(15))
        self.db_table = DBSet_Meta(self.name)
        self.session = Session(self.engine, future=True)
        self.session.add(self.db_table)
        self.session.commit()
        self.db_table.entry_class.__table__.create(bind=self.engine, checkfirst=True)
        # print("CREATED TABLE", self.db_table.entry_class.__table__)
        if isinstance(iter, DBSet):
            self.update(iter)
        else:
            self.session.bulk_save_objects([self.db_table.entry_class(value) for value in set(iter)])
            self.session.commit()
            # for item in iter:
            #     self.add(item)

    def add(self, value: _T) -> None:
        try:
            DBSet_Hash(value)
            value == 0
            entry = self.db_table.entry_class(value)
            self.session.add(entry)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            pass

    def _add_no_commit(self, value: _T) -> None:
        try:
            entry = self.db_table.entry_class(value)
            self.session.add(entry)
        except IntegrityError:
            self.session.rollback()
            pass

    def _drop(self):
        self.db_table.entry_class.__table__.drop(self.engine)

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        if self.db_url == "sqlite:///:memory:?blank":
            return DBSet(self)
        else:
            return DBSet(self, db_url=self.engine.url)

    def __getstate__(self):
        state = {}
        state['name'] = self.name
        state['db_url'] = self.db_url
        return state

    def __setstate__(self, state):
        self.name = state['name']
        self.db_url = state['db_url']
        if self.db_url != "sqlite:///:memory:?blank":
            self.engine = create_engine(self.db_url, echo=False, future=True)
        else:
            DB_URI = 'file::memory:?cache=shared'
            PY2 = sys.version_info.major == 2
            if PY2:
                params = {}
            else:
                params = {'uri': True}

            creator = lambda: sqlite3.connect(DB_URI, **params)
            self.engine = create_engine(self.db_url, echo=False, future=True,
                                        creator=creator)
        Base.metadata.create_all(self.engine, checkfirst=True)
        self.db_table = DBSet_Meta(self.name)
        self.db_table.entry_class.__table__.create(bind=self.engine, checkfirst=True)
        self.session = Session(self.engine, future=True)

    def __eq__(self, other):
        if not isinstance(other, Set):
            return False
        if len(self) != len(other):
            return False
        # print("We are instance of set ish")
        for item in self:
            if item not in other:
                return False
        for item in other:
            if item not in self:
                return False
        return True

    def __repr__(self):
        if len(self) == 0:
            return 'dbset()'
        else:
            return f'{{{", ".join(map(str, self))}}}'

    def update(self, *others):
        for other in others:
            if isinstance(other, DBSet) and other.db_url == self.db_url:
                # print("Adding from DBSet")
                i = insert(self.db_table.entry_class).from_select((other.db_table.entry_class.element_id,
                                                                   other.db_table.entry_class.hash,
                                                                   other.db_table.entry_class.data),
                                                                  other.session.query(
                                                                      other.db_table.entry_class).filter(
                                                                      ~exists().where(
                                                                          other.db_table.entry_class.hash == self.db_table.entry_class.hash).where(
                                                                          other.db_table.entry_class.data == self.db_table.entry_class.data)))
                self.session.execute(i)
                self.session.commit()
            else:
                for item in set(other):
                    self.add(item)
                # self.session.commit()

    def intersection_update(self, *others):
        for other in others:
            if isinstance(other, DBSet) and other.db_url == self.db_url:
                # print("Removing from DBSet")
                d = delete(self.db_table.entry_class).filter(
                    ~exists().where(other.db_table.entry_class.hash == self.db_table.entry_class.hash). \
                        where(other.db_table.entry_class.data == self.db_table.entry_class.data)).execution_options(
                    synchronize_session=False)
                # print(d)
                self.session.execute(d)
                self.session.commit()
            else:
                d = delete(self.db_table.entry_class).filter(~self.db_table.entry_class.data.in_(set(other)))
                self.session.execute(d)
                self.session.commit()
                # newset = self.copy()
                # newset.clear()
                # for item in other:
                #     if item in self:
                #         newset.add(item)
                # self.clear()
                # self.update(newset)

    def difference_update(self, *others):
        for other in others:
            if isinstance(other, DBSet):
                # print("Removing from DBSet")
                d = delete(self.db_table.entry_class).filter(
                    exists().where(other.db_table.entry_class.hash == self.db_table.entry_class.hash). \
                        where(other.db_table.entry_class.data == self.db_table.entry_class.data)).execution_options(
                    synchronize_session=False)
                # print(d)
                self.session.execute(d)
                self.session.commit()
            else:
                d = delete(self.db_table.entry_class).filter(self.db_table.entry_class.data.in_(set(other)))
                self.session.execute(d)
                self.session.commit()
                # for item in set(other):
                #     self.discard(item)
                # self.session.commit()

    def symmetric_difference_update(self, *others):
        for other in others:
            if isinstance(other, DBSet):
                newset = other.copy()
                newset.difference_update(self)
                self.difference_update(other)
                self.update(newset)
                newset._drop()
            else:
                newset = set()
                for item in set(other):
                    if item not in self:
                        newset.add(item)
                self.difference_update(other)
                self.update(newset)

    def union(self, *others):
        n = self.copy()
        n.update(*others)
        return n

    def intersection(self, *others):
        n = self.copy()
        n.intersection_update(*others)
        return n

    def symmetric_difference(self, *others):
        n = self.copy()
        n.symmetric_difference_update(*others)
        return n

    def difference(self, *others):
        n = self.copy()
        n.difference_update(*others)
        return n

    def clear(self):
        self.session.execute(delete(self.db_table.entry_class))
        self.session.commit()

    def isdisjoint(self, other: Iterable[Any]) -> bool:
        if isinstance(other, DBSet) and other.db_url == self.db_url:
            return self.session.query(self.db_table.entry_class).filter(
                exists().where(other.db_table.entry_class.hash == self.db_table.entry_class.hash).
                    where(other.db_table.entry_class.data == self.db_table.entry_class.data)).limit(1).count() == 0
            # return False
        else:
            s = set(other)
            return self.session.query(self.db_table.entry_class).filter(self.db_table.entry_class.data.in_(s)).limit(
                1).count() == 0 if len(s) > 0 else True
            # return True
            # for item in other:
            #     if item in self: return False
        # return True

    def issuperset(self, other):
        if isinstance(other, DBSet) and other.db_url == self.db_url:
            return other.session.query(other.db_table.entry_class).filter(
                ~exists().where(other.db_table.entry_class.hash == self.db_table.entry_class.hash).
                    where(other.db_table.entry_class.data == self.db_table.entry_class.data)).limit(
                1).count() == 0
        else:
            # s = set(other)
            # return self.session.query(other.db_table.entry_class).filter(
            #     ~self.db_table.entry_class.data.in_(s)).limit(1).count() == 0
            for item in other:
                if item not in self: return False
        return True

    def issubset(self, other):
        if isinstance(other, DBSet) and other.db_url == self.db_url:
            return self.session.query(self.db_table.entry_class).filter(
                ~exists().where(other.db_table.entry_class.hash == self.db_table.entry_class.hash).
                    where(other.db_table.entry_class.data == self.db_table.entry_class.data)).limit(
                1).count() == 0
        else:
            s = set(other)
            return self.session.query(self.db_table.entry_class).filter(
                ~self.db_table.entry_class.data.in_(s)).limit(1).count() == 0 if len(s) > 0 else False
        #     for item in self:
        #         if item not in other: return False
        # return True

    def __or__(self, other):
        if isinstance(other, Set):
            return self.union(other)
        else:
            raise TypeError()

    def __and__(self, other):
        if isinstance(other, Set):
            return self.intersection(other)
        else:
            raise TypeError()

    def __xor__(self, other):
        if isinstance(other, Set):
            return self.symmetric_difference(other)
        else:
            raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Set):
            return self.difference(other)
        else:
            raise TypeError()

    def __ge__(self, other):
        if isinstance(other, Set):
            return self.issuperset(other)
        else:
            raise TypeError()

    def __le__(self, other):
        if isinstance(other, Set):
            return self.issubset(other)
        else:
            raise TypeError()

    def __gt__(self, other):
        if isinstance(other, Set):
            return self.issuperset(other) and not self.issubset(other)
        else:
            raise TypeError()

    def __lt__(self, other):
        if isinstance(other, Set):
            return self.issubset(other) and not self.issuperset(other)
        else:
            raise TypeError()

    def __iand__(self, other):
        if isinstance(other, Set):
            self.intersection_update(other)
            return self
        else:
            raise TypeError()

    def __ior__(self, other):
        if isinstance(other, Set):
            self.update(other)
            return self
        else:
            raise TypeError()

    def __ixor__(self, other):
        if isinstance(other, Set):
            self.symmetric_difference_update(other)
            return self
        else:
            raise TypeError()

    def __isub__(self, other):
        if isinstance(other, Set):
            self.difference_update(other)
            return self
        else:
            raise TypeError()

    def __ror__(self, other):
        if isinstance(other, Set):
            return self.union(other)
        else:
            raise TypeError()

    def __rand__(self, other):
        if isinstance(other, Set):
            return self.intersection(other)
        else:
            raise TypeError()

    def __rxor__(self, other):
        if isinstance(other, Set):
            return self.symmetric_difference(other)
        else:
            raise TypeError()

    def __rsub__(self, other):
        if isinstance(other, Set):
            return self.difference(other)
        else:
            raise TypeError()
