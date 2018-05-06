
def thousands_with_commas(i):
    """
    Receive an integer and returns a string with the number
    with commas each three digits
    """

    if not type(i) == int:
        raise TypeError("Parameter must be an integer.")
	
        i = "{:,}".format(i)		
        return str(i)
	

if __name__ == '__main__':
    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
