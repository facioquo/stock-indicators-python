from enum import Enum, EnumMeta


class _ValueEnumMeta(EnumMeta):
    """
    EnumMeta that returns `value`.
    """
    def __getattribute__(cls, name):
        obj = super().__getattribute__(name)
        if isinstance(obj, Enum) and hasattr(obj, 'value'):
            obj = obj.value
        return obj

    def __getitem__(cls, name):
        member = super().__getitem__(name)
        if hasattr(member, 'value'):
            member = member.value
        return member

    def __call__(self, *args, **kwds):
        obj = super().__call__(*args, **kwds)
        if isinstance(obj, Enum) and hasattr(obj, 'value'):
            obj = obj.value
        return obj


class ValueEnum(Enum, metaclass=_ValueEnumMeta):
    """Enum class that returns `value`"""
