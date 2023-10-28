from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ["id", "name", "description", "price", "image_url", "stock"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    price: float
    image_url: str
    stock: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class ProductListResponse(_message.Message):
    __slots__ = ["products", "message"]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    message: str
    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class ProductListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProductRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ProductResponse(_message.Message):
    __slots__ = ["product", "message"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    product: Product
    message: str
    def __init__(self, product: _Optional[_Union[Product, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class ProductCreateRequest(_message.Message):
    __slots__ = ["name", "description", "price", "image_url", "stock"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    price: float
    image_url: str
    stock: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class ProductUpdateRequest(_message.Message):
    __slots__ = ["id", "name", "description", "price", "stock", "image_url"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    price: float
    stock: int
    image_url: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., stock: _Optional[int] = ..., image_url: _Optional[str] = ...) -> None: ...

class ProductDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ProductDeleteResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ProductSumPriceRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[_Iterable[int]] = ...) -> None: ...

class ProductSumPriceResponse(_message.Message):
    __slots__ = ["price"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: float
    def __init__(self, price: _Optional[float] = ...) -> None: ...
