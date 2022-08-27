from enum import IntEnum


class CsCompatibleIntEnum(IntEnum):
    def __init__(self, value) -> None:
        super().__init__()
        self.cs_value = value
