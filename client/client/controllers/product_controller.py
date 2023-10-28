from pyramid.view import view_config
from pyramid.response import Response
from client.grpc.product_client import ProductClient


@view_config(route_name="product", renderer="json")
def product(request):
    id = request.matchdict["id"]

    print(f"ID: {id}")

    try:
        product_client = ProductClient()
        result = product_client.get_product(id=1)
        return result
    except Exception as e:
        return Response(json_body={"error": {"message": str(e)}}, status=500)
