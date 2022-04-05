



def to_usd(my_price):
    """
    This is a docstring. It will tell us what this function is supposed to do. 
    This specific function will convert the passed parameter into a USD formatted value 
    Invoke like this: to_usd(9.999). The function will return $9.99
    """
    return '${:,.2f}'.format(my_price)

# unofficial testing:
# if this code is in the global scope
# ... of a file we are trying to import from
# ... it will throw errors
#price = input("Please choose a price like $4.999999")
#print(to_usd(float(price)))

# to fix this, we will do this:
# nesting the code in the main conditional will fix the errors we were being thrown
if __name__ == "__main__":
    price = input("Please choose a price like $4.999999")
    print(to_usd(float(price)))


