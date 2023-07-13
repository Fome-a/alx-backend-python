#!/usr/bin/env python3
"""a module 9-element_length.py, with let's duck type an iterable object"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the below function’s parameters
    and return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
