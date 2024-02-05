def calculator() -> None:
    selection = ('+', '-', '*', '/', 'pow', 'avg', 'quit')
    
    while True:
        show_selection(selection)
        break
        
        
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
    
    
    
if __name__ == "__main__":
    calculator()