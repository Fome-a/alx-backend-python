#!/usr/bin/env python3
"""a module 6-sum_mixed_list.py, with Complex types mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float.
    """
    return sum(mxd_lst)
