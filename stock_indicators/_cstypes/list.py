from collections import deque

from stock_indicators._cslib import CsList


class List:
    """
    Class for converting Python's iterator type into C#'s `System.Collections.Generic.List` class.

    Parameters:
        generic : generic type for `System.Collections.Generic.List`.

        sequence : iterator types. (e.g. `list`, `tuple`, `range`)

    See Also:
        [Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)

    Examples:
        Constructing `System.Collections.Generic.List` from `list` of Python.

        >>> py_list = [1, 2, 3]
        >>> cs_list = List(int, py_list)
        >>> cs_list
        System.Collections.Generic.List`1[System.Int32]

        Notice that It can be iterated like other iterable types in Python.

        >>> cs_list = List(int, [1, 2, 3])
        >>> for i in cs_list:
        >>>     print(i, end='')
        123
    """
    def __new__(cls, generic, sequence) -> CsList:
        cs_list = CsList[generic]()
        deque(map(cs_list.Add, sequence), maxlen=0)

        return cs_list
