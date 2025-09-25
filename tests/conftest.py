import pytest
import requests
from src.config_reader import read_config

@pytest.fixture(scope="session")
def config():
    return read_config()

@pytest.fixture(scope="session")
def base_url(config):
    return config.get("url", "https://httpbin.org")

@pytest.fixture
def http_client():
    with requests.Session() as session:
        yield session

@pytest.fixture
def retries(config):
    return config.get("retries", 3)

