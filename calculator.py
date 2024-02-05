


def calculator():
    """
    Main function of the program!
    """
    selection = ["+", "-", "*", "/", "pow", "avg", "quit"]
    while True:
        show_selection(selection)
        break
    
    
def show_selection(*args: list) -> None:
    """
    Description:
    ------------
    Connects values from *args with .join method.
    Then adds separator before and after parameters.
    
    Example:
    --------
    args = ("a", "b", "c")
    
    Result:
    -------
    a | b | c
    ----------
    """
    joined = " | ".join(*args)
    sepatator = "-" * len(joined)
    print(sepatator, joined, sepatator, sep="/n")