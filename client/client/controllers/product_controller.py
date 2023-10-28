from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from client.grpc.product_client import ProductClient


# @view_config(route_name="product", renderer="json")
# def product(request):
#     print(request.GET.get("productId"))

#     try:
#         product_client = ProductClient()
#         result = product_client.get_product(id=1)
#         return result
#     except Exception as e:
#         return Response(json_body={"error": {"message": str(e)}}, status=500)


@view_defaults(route_name="product", renderer="json")
class ProductView:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            product_client = ProductClient()

            productId = self.request.GET.get("productId")

            if productId:
                result = product_client.get_product(id=int(productId))

                if result is None:
                    return Response(
                        json_body={"error": {"message": "Not found"}}, status=404
                    )

            else:
                result = product_client.get_products()

            return result

        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="POST")
    def post(self):
        if self.request.json_body.get("name") == None:
            return Response(
                json_body={"error": {"message": "Name is required"}}, status=400
            )
        try:
            product_client = ProductClient()
            result = product_client.create_product(
                name=self.request.json_body.get("name"),
                price=self.request.json_body.get("price") or 10000,
                description=self.request.json_body.get("description")
                or "No description",
                image_url=self.request.json_body.get("image_url") or "No image_url",
                stock=self.request.json_body.get("stock") or 10,
            )
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="PUT")
    def put(self):
        if self.request.json_body.get("id") == None:
            return Response(
                json_body={"error": {"message": "id is required"}}, status=400
            )

        try:
            product_client = ProductClient()

            selected_product = product_client.get_product(
                id=self.request.json_body.get("id")
            )

            if selected_product is None:
                return Response(
                    json_body={"error": {"message": "Not found"}}, status=404
                )

            result = product_client.update_product(
                id=self.request.json_body.get("id"),
                name=self.request.json_body.get("name"),
                price=self.request.json_body.get("price") or 10000,
                description=self.request.json_body.get("description")
                or "No description",
                image_url=self.request.json_body.get("image_url") or "No image_url",
                stock=self.request.json_body.get("stock") or 10,
            )
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="DELETE")
    def delete(self):
        if self.request.json_body.get("id") == None:
            return Response(
                json_body={"error": {"message": "id is required"}}, status=400
            )

        try:
            product_client = ProductClient()

            selected_product = product_client.get_product(
                id=self.request.json_body.get("id")
            )

            if selected_product is None:
                return Response(
                    json_body={"error": {"message": "Not found"}}, status=404
                )

            result = product_client.delete_product(id=self.request.json_body.get("id"))
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)


@view_config(route_name="sum_product_price", renderer="json", request_method="POST")
def sum_product_price(request):
    if request.json_body.get("id") == None:
        return Response(json_body={"error": {"message": "id is required"}}, status=400)

    if len(request.json_body.get("id")) == 0:
        return Response(json_body={"error": {"message": "id is required"}}, status=400)

    try:
        print(request.json_body.get("id"))
        product_client = ProductClient()
        result = product_client.sum_price_product(id=request.json_body.get("id"))
        return result
    except Exception as e:
        return Response(json_body={"error": {"message": str(e)}}, status=500)
