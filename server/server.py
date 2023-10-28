from concurrent import futures
import time
import logging
import grpc
import products_pb2
import products_pb2_grpc

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from models.product import Product


class ProductsServicer(products_pb2_grpc.ProductsServicer):
    def GetProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Product).where(Product.id == request.id)
                ).first()

                conn.commit()

            return products_pb2.ProductResponse(
                product=products_pb2.Product(
                    id=res[0],
                    name=res[1],
                    price=res[2],
                    description=res[3],
                    stock=res[4],
                    image_url=res[5],
                ),
                message="Product retrieved",
            )
        except Exception as e:
            print(f"Error fd {e}")
            return products_pb2.ProductResponse(message="Error")

    def GetProducts(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(select(Product).order_by(desc(Product.id))).all()

                products = []

                for row in res:
                    products.append(
                        products_pb2.Product(
                            id=row[0],
                            name=row[1],
                            price=row[2],
                            description=row[3],
                            stock=row[4],
                            image_url=row[5],
                        )
                    )

                conn.commit()

            return products_pb2.ProductListResponse(
                products=products,
                message="Products retrieved",
            )
        except Exception as e:
            print(f"Error df {e}")
            return products_pb2.ProductListResponse(message="Error")

    def CreateProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    insert(Product).values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        stock=request.stock,
                        image_url=request.image_url,
                    )
                )

                conn.commit()

            print(f"Product {request.name} created")

            return products_pb2.ProductResponse(
                product=products_pb2.Product(
                    name=request.name,
                    description=request.description,
                    price=request.price,
                    image_url=request.image_url,
                    stock=request.stock,
                ),
                message="Product created",
            )

        except Exception as e:
            print(f"Error sd {e}")
            return products_pb2.ProductResponse(message="Error")

    def UpdateProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    update(Product)
                    .where(Product.id == request.id)
                    .values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        stock=request.stock,
                        image_url=request.image_url,
                    )
                )

                conn.commit()

            print(f"Product {request.name} updated")

            return products_pb2.ProductResponse(
                product=products_pb2.Product(
                    id=request.id,
                    name=request.name,
                    description=request.description,
                    price=request.price,
                    image_url=request.image_url,
                    stock=request.stock,
                ),
                message="Product updated",
            )

        except Exception as e:
            print(f"Error as {e}")
            return products_pb2.ProductResponse(message="Error")

    def DeleteProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                conn.execute(delete(Product).where(Product.id == request.id))

                conn.commit()

            return products_pb2.ProductDeleteResponse(message="Product deleted")

        except Exception as e:
            print(f"Error as {e.with_traceback()}")
            return products_pb2.ProductDeleteResponse(message="Error")

    def SumPriceProducts(self, request, context):
        try:
            price = 0

            ids = request.id

            for id in ids:
                with engine.connect() as conn:
                    conn.begin()

                    res = conn.execute(select(Product).where(Product.id == id)).first()

                    if res is not None:
                        conn.execute(
                            update(Product)
                            .where(Product.id == id)
                            .values(stock=res[4] - 1)
                        )

                        price += res[2]

                    conn.commit()

            return products_pb2.ProductSumPriceResponse(
                price=price,
            )

        except Exception as e:
            print(f"Error df {e}")
            return products_pb2.ProductSumPriceResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    products_pb2_grpc.add_ProductsServicer_to_server(ProductsServicer(), server)
    server.add_insecure_port("localhost:6000")
    server.start()
    print("Server started at localhost:6000")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
