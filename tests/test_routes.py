import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    return app.test_client()

def test_homepage_route_loads_successfully(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"SIT707 Quality Tracker" in response.data

def test_dashboard_route_loads_successfully(client):
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Quality Dashboard" in response.data

def test_health_route_returns_healthy_json(client):
    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert data["service"] == "SIT707 Quality Tracker"

def test_dashboard_rejects_empty_form_submission(client):
    response = client.post(
        "/dashboard",
        data={
            "test_name": "",
            "module_name": "Authentication",
            "status": "Pass",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Test name is required" in response.data
