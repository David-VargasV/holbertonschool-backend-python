#!/usr/bin/env python3

""" Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier
    that takes a float multiplier as argument
    and returns a function that multiplies a
    float by multiplier.
    """
    def multi_float(n: float) -> float:
        """
        Function that multiplies a float by multiplier.
        """
        return (n * multiplier)

    return (multi_float)
