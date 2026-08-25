import pytest
from utils.test_data import API_BASE_URL


@pytest.mark.api
class TestApi:
    def test_get_users_list(self, api_client):
        response = api_client.get(f"{API_BASE_URL}/api/users", params={"page": 1}, timeout=10)
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data.get("data"), list)
        assert len(data["data"]) > 0

        first_user = data["data"][0]
        assert "id" in first_user and "email" in first_user

    def test_get_user_not_found(self, api_client):
        response = api_client.get(f"{API_BASE_URL}/api/users/9999", timeout=10)
        assert response.status_code == 404

    def test_create_user(self, api_client):
        payload = {"name": "Marat", "job": "QA Engineer"}
        response = api_client.post(f"{API_BASE_URL}/api/users", json=payload, timeout=10)
        assert response.status_code == 201

        body = response.json()
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]
        assert "id" in body