from sqlalchemy import (
    Table, MetaData, Column, Integer, String
)
from sqlalchemy.orm import mapper

import barky


metadata = MetaData()

# table mapping to the bookmark database
bookmarks = Table(
    'bookmarks', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=False),
    Column('url', Integer, nullable=False),
    Column('notes', String(255)),
    Column('date_added', String(255), nullable=False),
)


def start_mappers():
    mapper(barky.Bookmark, bookmarks)
