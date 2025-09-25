import yaml
import os

def read_config(path="config.yaml"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found at {path}")
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config

if __name__ == "__main__":
    config = read_config()
    print("API URL:", config.get("url"))
    print("Retries:", config.get("retries"))

