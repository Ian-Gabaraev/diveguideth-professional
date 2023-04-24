import os

TRUTHY = ("True", "TRUE", "true", True, 1, "1")
DOCKERIZED = os.environ.get("DOCKERIZED", False) in TRUTHY

if DOCKERIZED:
    API_HOST = os.environ.get("API_HOST")
    API_PORT = os.environ.get("API_PORT")
else:
    API_HOST = "http://127.0.0.1"
    API_PORT = "8000"

API_HEALTH_CHECK_ROUTE = "util/health/check"

HEALTHY_CACHE_KEY = "healthy"


def get_api_url():
    if not API_HOST or not API_PORT:
        return None

    return f"http://{API_HOST}:{API_PORT}"
