# roots.py

def quad_roots(a=1.0, b=2.0, c=0.0):
    """Returns the roots of a quadratic equation: ax^2 + bx + c.

    INPUTS
    =======
    a: float, optional, default value is 1
       Coefficient of quadratic term
    b: float, optional, default value is 2
       Coefficient of linear term
    c: float, optional, default value is 0
       Constant term

    RETURNS
    ========
    roots: 2-tuple of complex floats
       Has the form (root1, root2) unless a = 0 
       in which case a ValueError exception is raised

    NOTES
    =====
    PRE: 
         - a, b, c have numeric type
         - three or fewer inputs
    POST:
         - a, b, and c are not changed by this function
         - raises a ValueError exception if a = 0
         - returns a 2-tuple of roots

    EXAMPLES
    =========
    >>> quad_roots(1.0, 1.0, -12.0)
    ((3+0j), (-4+0j))
    """
    import cmath # Can return complex numbers from square roots
    if a == 0:
        raise ValueError("The quadratic coefficient is zero.  This is not a quadratic equation.")
    else:
        sqrt_disc = cmath.sqrt(b * b - 4.0 * a * c)
        r1 = -b + sqrt_disc
        r2 = -b - sqrt_disc
        two_a = 2.0 * a
        return (r1 / two_a, r2 / two_a)

def linear_roots(a=1.0, b=0.0):
    """Returns the roots of a linear equation: ax+ b = 0.
    
    INPUTS
    =======
    a: float, optional, default value is 1
       Coefficient of linear term
    b: float, optional, default value is 0
       Coefficient of constant term
    
    RETURNS
    ========
    roots: 1-tuple of real floats
       Has the form (root) unless a = 0 
       in which case a ValueError exception is raised
    
    EXAMPLES
    =========
    >>> linear_roots(1.0, 2.0)
    -2.0
    """
    if a == 0:
        raise ValueError("The linear coefficient is zero.  This is not a linear equation.")
    else:
        return ((-b / a))