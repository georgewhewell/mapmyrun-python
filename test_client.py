import pytest
from runstat.client import Client

TEST_KEY = 'test key'
TEST_SECRET = 'test secret'

def test_arguemnts_required():
    with pytest.raises(Exception):
        Client()

def test_can_make_client():
    assert Client('app key', 'app secret')

@pytest.fixture
def client():
    return Client(TEST_KEY, TEST_SECRET)

def test_can_get_login(client):
    assert client.get_redirect()
