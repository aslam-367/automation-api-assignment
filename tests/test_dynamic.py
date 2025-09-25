from src.faker_utils import fake_user

def test_post_random_user(http_client, base_url):
    user = fake_user()
    resp = http_client.post(f"{base_url}/post", json=user)
    assert resp.status_code == 200
    assert resp.json()["json"] == user
    
