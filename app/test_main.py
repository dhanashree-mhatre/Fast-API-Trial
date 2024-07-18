from fastapi.testclient import TestClient
from .main import app


client=TestClient(app)

def testread():
    response=client.get('/')
    assert response.status_code==200
    assert response.json()=={"message":"hello world"}

def test_read_item():
    response=client.get('/items/1')
    assert response.status_code==200
    assert response.json()=={'item':{'id':1,'name':'string','description':'string','price':0.0}}

def test_post_item():
    response=client.post('/items/items',json={'name':'watch','description':'luxury','price':1000})
    assert response.status_code==200
    assert response.json()=={'id':4,'name':'watch','description':'luxury','price':1000.0}