from urllib.parse import urljoin
import logging

import requests
from . import settings

logging.basicConfig(level=logging.DEBUG)


def is_api_healthy():
    try:
        if (api_url := settings.get_api_url()) is None:
            raise ValueError("API_HOST or API_PORT are undefined")

        url = urljoin(api_url, settings.API_HEALTH_CHECK_ROUTE)
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("API is healthy")
            return True
        else:
            logging.debug(
                f"API returned unhealthy status {response.status_code}. " f"URL: {url}"
            )
            return False
    except requests.exceptions.RequestException as e:
        logging.error(
            f"RequestException thrown trying to connect to API. "
            f"URL: {url}. "
            f"Exception: {str(e)}"
        )
        return False
