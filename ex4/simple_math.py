"""
A collection of simple math operations
"""


def simple_add(a,b):
    """
    Returns the result of the function a + b

    Parameters
    ----------
    a : float
        input as the first summand of the function a + b
    b : float
        input as the second summand of the function a + b

        
    Returns
    -------
    f(x) : float
        the result of the function f(x) = a + b

        
    Examples
    --------
    >>> simple_add(2, 4)
    6
    >>> simple_add(2.3, 4.5)
    6.8
    """
    return a+b


def simple_sub(a,b):
    """
    Returns the result of the function a - b

    Parameters
    ----------
    a : float
        input as the minuend of the function a - b
    b : float
        input as the subtrahend of the function a - b

    Returns
    -------
    f(x) : float
        the result of the function f(x) = a - b


    Examples
    --------
    >>> simple_sub(4, 3)
    1
    >>> simple_sub(4.3, 1.5)
    2.8
    """
    return a-b



def simple_mult(a,b):
    """
    Returns the result of the function a * b

    Parameters
    ----------
    a : float
        input as the first factor of the function a * b
    b : float
        input as the second factor of the function a * b
    
    Returns
    -------
    f(x) : float
        the result of the function f(x) = a * b

    Examples
    --------
    >>> simple_mult(4, 3)
    12
    >>> simple_mult(-4, 1.5)
    -6
    """
    return a*b



def simple_div(a,b):
    """
    Returns the result of the function a / b

    Parameters
    ----------
    a : float
        input as the numerator of the function a / b
    b : float
        input as the denominator of the function a / b

    Returns
    -------
    f(x) : float
        the result of the function f(x) = a / b

    Examples
    --------
    >>> simple_div(4, 2)
    2
    >>> simple_div(-4.5, 1.5)
    -3
    """
    return a/b



def poly_first(x, a0, a1):
    """
    Returns the result of the linear polynomial a0 + a1 * x

    Parameters
    ----------
    a0 : float
        offset parameter to the linear polynomial a0 + a1 * x
    a1 : float
        slope parameter to the linear polynomial a0 + a1 * x
    x : float
        argument to the linear polynomial f(x) = a0 + a1 * x

    Returns
    -------
    f(x) : float
        the result of the function f(x) = a0 + a1 * x 

    Examples
    --------
    >>> simple_div(4, 2, 3)
    14
    >>> simple_div(-4.5, 1.5, 3)
    -12
    """
    return a0 + a1*x



def poly_second(x, a0, a1, a2):
    """
    Returns the result of the quadratic polynomial a0 + a1 * x + a2 * x**2

    Parameters
    ----------
    a0 : float
        offset parameter to the quadratic polynomial a0 + a1 * x + a2 * x**2
    a1 : float
        slope parameter to the quadratic polynomial a0 + a1 * x + a2 * x**2
    a2 : float
        quadratic parameter to the quadratic polynomial a0 + a1 * x + a2 * x**2
    x : float
        argument to the quadratic polynomial f(x) = a0 + a1 * x + a2 * x**2

    Returns
    -------
    f(x) : float
        the result of the function f(x) = a0 + a1 * x + a2 * x**2

    Examples
    --------
    >>> simple_div(4, 2, 3, 1)
    14
    >>> simple_div(-4.5, 1.5, 3, 1)
    8.25
    """
    return poly_first(x, a0, a1) + a2*(x**2)
