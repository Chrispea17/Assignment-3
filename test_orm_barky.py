from cmath import exp
from datetime import date
import barky
import pprint


def test_bookmark_mapper_can_load_bookmarks(session):
    session.execute(
        'INSERT INTO bookmarks (title, url, notes, date_added) VALUES '
        '("searchengine1", "google.com", "none" ,"02-15-2022"),'
        '("searchengine2", "duck-duck-go.com", "Better","02-15-2022")'

    )
    expected = [
        barky.Bookmark("searchengine1", "google.com", "none", "02-15-2022"),
        barky.Bookmark("searchengine2", "duck-duck-go.com",
                       "Better", "02-15-2022"),
    ]
    
    pretprint = pprint.PrettyPrinter()
    pretprint.pprint(expected)
    assert session.query(barky.Bookmark).all() == expected
    session.close()
    session = None


def test_bookmark_mapper_can_save_bookmarks(session):
    new_bookmark = barky.Bookmark(
        "searchengine2", "duck-duck-go.com", "Better", "02-15-2022")
    session.add(new_bookmark)
    session.commit()

    rows = list(session.execute(
        'SELECT title, url, notes, date_added FROM bookmarks'))
    assert rows == [
        ("searchengine2", "duck-duck-go.com", "Better", "02-15-2022")]
    session.close()
    session = None


def test_retrieving_bookmarks(session):
    session.execute(
        'INSERT INTO bookmarks (title, url, notes, date_added)'
        ' VALUES ("order1", "duck-duck-go.com", "Boring", "02-15-2022")'
    )
    session.execute(
        'INSERT INTO bookmarks (title, url, notes, date_added)'
        ' VALUES ("order2", "google.com", 200, "2011-04-11")'
    )
    expected = [
        barky.Bookmark("order1", "duck-duck-go.com", "Boring", "02-15-2022"),
        barky.Bookmark("order2", "google.com", "200", "2011-04-11"),
    ]

    assert session.query(barky.Bookmark).all() == expected
    session.close()
    session = None
