from math import sqrt

import pandas as pd


def add(a: int, b: int) -> int:
    """Add two numbers and return the result.

    .. math::
       a + b = c

    Args :
        a (int) : first integer
        b (int) : second integer

    Returns :
        sum of the two integers
    """
    return a + b


def sub(a: int, b: int) -> int:
    """Subtract two numbers and return the result.

    .. math::
       a - b = c

    Args :
        a (int) : first integer
        b (int) : second integer

    Returns :
        substraction of the two integers
    """
    return a - b


def square(a: int) -> float:
    """Subtract two numbers and return the result.

    .. math::
       sqrt(a) = c

    Args :
        a (int) : number to be squared

    Returns :
        root sqare of the number
    """
    if a < 0:
        ValueError("Cannot compute square root of negative number")

    return sqrt(a)


def print_data(df: pd.DataFrame):
    """Print the content of a DataFrame in the terminal.

    Args :
        df (pd.DataFrame) : the DataFrame to be printed
    Returns :
        None
    """
    print(df)
