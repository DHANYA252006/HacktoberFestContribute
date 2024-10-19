#modified code
#!/usr/bin/python3

"""
Python functions to calculate Fibonacci series with additional features.
"""

def fibonacciAtIndex(index):
    """
    Returns the fibonacci number at a given index.
    Algorithm is using 3 variables instead of recursion to reduce memory usage and runtime.
    Includes handling for negative indices.
    """
    if index < 0:
        return "Invalid input: Index must be a non-negative integer."
    elif index == 0:
        return 0
    elif index == 1 or index == 2:
        return 1

    a1, a2 = 1, 1
    while index > 2:
        a1, a2 = a2, a1 + a2
        index -= 1
    return a2


def fibonacciUntilIndex(index, return_list=False):
    """
    Prints the fibonacci series up until a given index (included).
    Adds a return_list feature to return the Fibonacci series as a list instead of printing.
    Algorithm is using 3 variables instead of recursion in order to reduce memory usage and runtime.
    """
    if index < 1:
        raise ValueError("Index must be a positive integer.")

    a1 = 0
    a2 = 1
    position = 1
    fib_sequence = []  # List to store the sequence if required
    
    while position <= index:
        a1, a2 = a2, a1 + a2
        if return_list:
            fib_sequence.append(a1)
        else:
            print(f"Fibonacci number at index {position} = {a1}")
        position += 1
    
    if return_list:
        return fib_sequence

# Example usage of the functions
try:
    num = int(input("Enter an index to find the Fibonacci number at that index: "))
    print(f"Fibonacci number at index {num} = {fibonacciAtIndex(num)}")
    
    num_series = int(input("Enter an index to print the Fibonacci series until that index: "))
    series = fibonacciUntilIndex(num_series, return_list=True)
    print(f"Fibonacci series until index {num_series}: {series}")
    
except ValueError as e:
    print(f"Error: {e}")
