import json
import pytest
from AppVecinos import create_app

TEST_TOKEN = "test-token"
AUTH_HEADER = {"Authorization": f"Bearer {TEST_TOKEN}"}


@pytest.fixture
def client():
    app = create_app(config={"TESTING": True, "API_TOKEN": TEST_TOKEN})
    with app.test_client() as client:
        yield client


class TestGetNeighbors:
    def test_get_neighbors_without_authentication_returns_401(self, client):
        response = client.get("/api/neighbors")
        assert response.status_code == 401

    def test_get_neighbors_with_invalid_token_returns_401(self, client):
        response = client.get(
            "/api/neighbors",
            headers={"Authorization": "Bearer invalid-token"},
        )
        assert response.status_code == 401

    def test_get_neighbors_with_valid_token_returns_200(self, client):
        response = client.get("/api/neighbors", headers=AUTH_HEADER)
        assert response.status_code == 200

    def test_get_neighbors_returns_list(self, client):
        response = client.get("/api/neighbors", headers=AUTH_HEADER)
        data = json.loads(response.data)
        assert isinstance(data, list)

    def test_get_neighbors_returns_expected_fields(self, client):
        response = client.get("/api/neighbors", headers=AUTH_HEADER)
        data = json.loads(response.data)
        assert len(data) == 3
        neighbor = data[0]
        assert "id" in neighbor
        assert "name" in neighbor
        assert "apartment" in neighbor
