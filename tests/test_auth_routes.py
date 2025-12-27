def test_login_invalid_payload(client):
    response = client.post("/auth/login", json={})
    assert response.status_code in (400, 401)
