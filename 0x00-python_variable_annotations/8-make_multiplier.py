#!/usr/bin/env python3
"""a module 8-make_multiplier.py with Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a
    function that multiplies a float by multiplier.
    """

    def multiplier_func(number: float) -> float:
        return multiplier * number

    return multiplier_func
