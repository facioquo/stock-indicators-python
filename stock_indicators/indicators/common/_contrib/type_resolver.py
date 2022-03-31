from typing import Type, TypeVar, cast

_T = TypeVar("_T")
def generate_cs_inherited_class(child: Type[_T], cs_parent: Type):
    return cast(Type[_T] , type("_Wrapper", (cs_parent, ), dict(child.__dict__)))
