



def to_usd(my_price):
    """
    This is a docstring. It will tell us what this function is supposed to do. 
    This specific function will convert the passed parameter into a USD formatted value 
    Invoke like this: to_usd(9.999). The function will return $9.99
    """
    return '${:,.2f}'.format(my_price)
