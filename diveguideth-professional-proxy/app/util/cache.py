import redis
import os
import logging

logging.basicConfig(level=logging.INFO)


def get_redis_conn():
    redis_host = os.environ["REDIS_HOST"]
    redis_port = os.environ["REDIS_PORT"]
    logging.info(f"Attempting Redis connection @ {redis_host}:{redis_port}")
    redis_password = os.environ.get("REDIS_PWD", "")
    redis_db = 0
    redis_client = redis.Redis(
        host=redis_host, port=redis_port, password=redis_password, db=redis_db
    )

    if redis_client.ping():
        logging.info("Connection to Redis server established")
        return redis_client
    else:
        logging.info("Connection to Redis server failed")


conn = get_redis_conn()
