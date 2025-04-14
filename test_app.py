import os
import pytest
from app import create_app, db

TEST_DB_URI = "sqlite:///test_tasks.db"


@pytest.fixture
def client():
    # Configurar la app con SQLite en archivo
    app = create_app("development")
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": TEST_DB_URI,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    # Crear base de datos real antes del test
    with app.app_context():
        db.create_all()

    # Usar el cliente de prueba
    with app.test_client() as client:
        yield client

    # Borrar archivo de base de datos después del test
    if os.path.exists("test_tasks.db"):
        os.remove("test_tasks.db")


def test_insert_data(client):
    response = client.post('/data', json={"name": "pytest_test"})
    assert response.status_code in [200, 409]


def test_get_data(client):
    client.post('/data', json={"name": "pytest_test_2"})
    response = client.get('/data')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_delete_data(client):
    client.post('/data', json={"name": "to_delete"})
    data_list = client.get('/data').get_json()
    to_delete_id = next((d["id"] for d in data_list if d["name"] == "to_delete"), None)
    assert to_delete_id is not None
    response = client.delete(f'/data/{to_delete_id}')
    assert response.status_code == 200
