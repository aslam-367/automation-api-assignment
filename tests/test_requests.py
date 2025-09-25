
def test_request_headers(http_client, base_url):
    resp = http_client.get(f"{base_url}/headers")
    headers = resp.json().get("headers", {})
    assert "Host" in headers

def test_inspect_get(http_client, base_url):
    resp = http_client.get(f"{base_url}/get")
    result = resp.json()
    assert result["url"].startswith(base_url)
