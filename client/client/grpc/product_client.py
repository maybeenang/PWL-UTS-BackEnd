import logging

import grpc
import client.grpc.products_pb2_grpc as products_pb2_grpc
import client.grpc.products_pb2 as products_pb2


# def run():
#     # NOTE(gRPC Python Team): .close() is possible on a channel and should be
#     # used in circumstances in which the with statement does not fit the needs
#     # of the code.
#     print("Will try to greet world ...")
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = products_pb2_grpc.ProductsStub(channel)
#         response = stub.DeleteProduct(products_pb2.ProductDeleteRequest(id=2))

#     print(f"Greeter client received: {response}")


# if __name__ == "__main__":
#     logging.basicConfig()
#     run()


class ProductClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5000

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = products_pb2_grpc.ProductsStub(self.channel)

    def create_product(self, name, price, description, image_url, stock):
        response = self.stub.CreateProduct(
            products_pb2.ProductCreateRequest(
                name=name,
                price=price,
                description=description,
                image_url=image_url,
                stock=stock,
            )
        )
        return dict(
            id=response.product.id,
            name=response.product.name,
            price=response.product.price,
            description=response.product.description,
            image_url=response.product.image_url,
            stock=response.product.stock,
        )

    def get_product(self, id):
        response = self.stub.GetProduct(products_pb2.ProductRequest(id=id))

        return dict(
            id=response.product.id,
            name=response.product.name,
            price=response.product.price,
            description=response.product.description,
            image_url=response.product.image_url,
            stock=response.product.stock,
        )

    def get_products(self):
        response = self.stub.GetProducts(products_pb2.ProductListRequest())

        return [
            dict(
                id=product.id,
                name=product.name,
                price=product.price,
                description=product.description,
                image_url=product.image_url,
                stock=product.stock,
            )
            for product in response.products
        ]

    def update_product(self, id, name, price, description, image_url, stock):
        response = self.stub.UpdateProduct(
            products_pb2.ProductUpdateRequest(
                id=id,
                name=name,
                price=price,
                description=description,
                image_url=image_url,
                stock=stock,
            )
        )
        return response

    def delete_product(self, id):
        response = self.stub.DeleteProduct(products_pb2.ProductDeleteRequest(id=id))
        return response
