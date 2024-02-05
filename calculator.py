import os


def calculator() -> None:
    selection = ('+', '-', '*', '/', 'pow', 'avg', 'quit')
    
    while True:
        show_selection(selection)
        
        choice = input("Select matmematical operation: ")
        os.system("clear")
        
        if choice == "quit":
            print("Goodbye")
            break
        elif choice == "pow":
            power()
        elif choice == "avg":
            average()
        elif choice == "+" or "-" or "*" or "/":
            arithmetic_operations()
        
        
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
    while True:
        base_input = (input("Base: "))
        exp_input = (input("Exponent: "))
        
        if base_input.isdigit() and exp_input.isdigit():
            base = float(base_input)
            exp = float(exp_input)
            break
        else:
            print("Enter a digit!")
    print(base ** exp)
        

def average() -> None:
    """
    Description:
    Takes values from input and stores them to list.
    Values must be numeric.
    If input '=', func calculates average as sum/lengh of list.
        
    Example:
    numbers = [1, 2, 3, 4, 5]

    Result:
    Average = 3
    """
    numbers = []
    
    while (value := input("Number: ")) != "=":
        if value.isnumeric():
            numbers.append(int((value)))
    result = sum(numbers) / len(numbers)
    print(result)


def arithmetic_operations() -> None:
    entry = ""
    
    while True:
        button = input("Select number or operator, '=' for result: ")
        
        if button.isnumeric() or button in ('+', '-', '*', '/'):
            entry += button
        elif button == "=":
            print(f'{entry} = {eval(entry)}')
            break
        
              
if __name__ == "__main__":
    calculator()