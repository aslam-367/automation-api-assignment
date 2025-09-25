
def test_json_response_format(http_client, base_url):
    resp = http_client.get(f"{base_url}/json")
    assert resp.headers["Content-Type"].startswith("application/json")
    assert isinstance(resp.json(), dict)

def test_status_code(http_client, base_url):
    resp = http_client.get(f"{base_url}/status/201")
    assert resp.status_code == 201
