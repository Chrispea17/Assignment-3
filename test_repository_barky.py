# pylint: disable=protected-access
import barky
import repository


def test_repository_can_save_a_bookmark(session):
    bookmark = barky.Bookmark(
        "order1", "duck-duck-go.com", "Boring", "02-15-2022")

    repo = repository.SqlAlchemyRepository(session)
    repo.add(bookmark)
    session.commit()

    rows = list(
        session.execute(
            'SELECT title, url, notes, date_added FROM "bookmark"'
        )
    )
    assert rows == [("order1", "duck-duck-go.com", "Boring", "02-15-2022")]


# def insert_bookmark(session):
#     session.execute(
#         "INSERT INTO order_lines (orderid, sku, qty)"
#         ' VALUES ("order1", "GENERIC-SOFA", 12)'
#     )
#     [[orderline_id]] = session.execute(
#         "SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sku",
#         dict(orderid="order1", sku="GENERIC-SOFA"),
#     )
#     return orderline_id
