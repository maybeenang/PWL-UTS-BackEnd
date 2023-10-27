import logging

import grpc
import products_pb2
import products_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = products_pb2_grpc.ProductsStub(channel)
        response = stub.DeleteProduct(products_pb2.ProductDeleteRequest(id=2))

    print(f"Greeter client received: {response}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
