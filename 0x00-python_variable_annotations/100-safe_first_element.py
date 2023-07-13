#!/usr/bin/env python3
"""a module 101-safely_get_value.py, with More involved type annotations"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the following code with the correct duck-typed annotations:"""
    if lst:
        return lst[0]
    else:
        return None
