from typing import Type, TypeVar, cast

_T = TypeVar("_T")
def generate_cs_inherited_class(child: Type[_T], cs_parent: Type, class_name="_Wrapper"):
    return cast(Type[_T], type(class_name, (cs_parent, ), {attr: getattr(child, attr) for attr in  dir(child)}))
