from django.http import HttpResponse
from django.db import connections
import logging

logging.basicConfig(level=logging.INFO)


def health_check(request):
    logging.info("Health check request received")
    return HttpResponse(status=200)


def db_health_check(request):
    logging.info("DB health check request received")
    if check_db_connection():
        return HttpResponse(status=200)
    return HttpResponse(status=500)


def check_db_connection():
    try:
        # get the default database connection
        conn = connections["default"]
        # use the exists() method to perform a lightweight operation
        conn.cursor().execute("SELECT 1")
        return True
    except Exception:
        return False
