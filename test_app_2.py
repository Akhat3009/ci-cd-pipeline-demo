import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, CI/CD Pipeline!" in response.data

def test_404_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
