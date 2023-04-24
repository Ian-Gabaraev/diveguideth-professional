from concurrent import futures
import grpc
from util import cache
import requests
from util import is_api_healthy, settings
import logging

import professional_unary_pb2_grpc as pb2_grpc
import professional_unary_pb2 as pb2
from urllib.parse import urljoin

logging.basicConfig(level=logging.DEBUG)


class UnaryService(pb2_grpc.ProfessionalUnaryServicer):
    def __int__(self, *args, **kwargs):
        ...

    def GetProContactInfo(self, request, context):
        logging.info("gRPC server has incoming request")
        if not is_api_healthy():
            logging.info(
                "GetProContactInfo API is unhealthy. Falling back to local cache."
            )
            if (cached := cache.conn.get(request.pro_id)) is not None:
                logging.info("Cache hit. Fallback successful.")
                return cached
            else:
                logging.info("Cache miss. Fallback failed.")
                return None

        contact_details_method_url = f"api/pro/{request.pro_id}/contact_info/"
        api_domain = settings.get_api_url()
        url = urljoin(api_domain, contact_details_method_url)
        response = requests.get(url)
        result = response.json()

        logging.info(f"Received from API: {result}")

        if result:
            cache.conn.set(request.pro_id, str(result), 3600)

        return pb2.ContactDetails(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ProfessionalUnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
