import pytest
import rawgql

def test_string_query():
    raw_gql.GQL_FOLDER = 'tests/gql/'
    query = """
        {
            users {
                id
                name
            }
        }
    """
    db = raw_gql.GraphQL('https://us1.prisma.sh/james-williams-a19027/test-db/dev')
    r = db.query(query)

    assert type(r) is dict
    assert type(r['data']['users']) is list


def test_file_query():
    raw_gql.GQL_FOLDER = 'tests/gql/'
    query = 'q_users.gql'
    db = raw_gql.GraphQL('https://us1.prisma.sh/james-williams-a19027/test-db/dev')
    r = db.query(query)

    assert type(r) is dict
    assert type(r['data']['users']) is list


def test_variables_query():
    raw_gql.GQL_FOLDER = 'tests/gql/'
    query = 'q_var_user.gql'
    vars = {'name': 'James Williams'}
    db = raw_gql.GraphQL('https://us1.prisma.sh/james-williams-a19027/test-db/dev')
    r = db.query(query, vars)

    assert type(r) is dict
    assert type(r['data']['users']) is list
    assert r['data']['users'][0]['name'] == 'James Williams'

