def calculator() -> None:
    selection = ('+', '-', '*', '/', 'pow', 'avg', 'quit')
    
    while True:
        show_selection(selection)
        
        choice = input("")
        
        
def show_selection(*args) -> None:
    """
    Description:
    Connects values from *args with .join method.
    Then adds separator before and after arguments.
    
    Example: 
    args = ("a", "b", "C")

    Result:
    ---------
    a | b | C
    ---------
    """    
    joined = ' | '.join(*args)
    separator = '-' * len(joined)
    print(separator, joined, separator, sep="\n")
    
    
def power() -> None:    
    """
    Description:
    Takes two inputs as parameters:
    1. input is base
    2. input is exponent
    
    Example:
    base = 5
    exp = 2

    Result:
    25
    """
    base = float(input("Base: "))
    exp = float(input("Exponent: "))
    print(base ** exp)
    
if __name__ == "__main__":
    calculator()