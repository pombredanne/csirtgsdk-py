import pytest

from whitefacesdk.feed import Feed
from whitefacesdk.client import Client

@pytest.fixture
def client():
    return Client()


def test_feed(client):
    f = Feed(client)

    assert f.client