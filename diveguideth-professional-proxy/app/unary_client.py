import grpc

import professional_unary_pb2_grpc as pb2_grpc
import professional_unary_pb2 as pb2


class UnaryClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )

        self.stub = pb2_grpc.ProfessionalUnaryStub(self.channel)

    def get_url(self, message):
        pro_id = pb2.ProId(pro_id=message)
        return self.stub.GetProContactInfo(pro_id)


client = UnaryClient()

for i in range(4_000):
    result = client.get_url(message=1)

