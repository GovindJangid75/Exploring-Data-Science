# Problem statement:
# 1. Functions can have default parameters and return values.
# 2. Functions can have docstrings which describe what the function does.
# 3. Python provides built-in attributes like __doc__ and __name__ for functions.
# 4. Help function shows documentation of built-in functions.
# 5. Example of a function with parameters, default values, docstring, and multiple return values.

def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    chai = "ginger"  # local variable, unrelated to return value
    return flavor  # function returns the flavor argument

print(chai_flavor.__doc__)   # Prints the docstring of function
print(chai_flavor.__name__)  # Prints the function name

help(len)  # Shows documentation for built-in len() function

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message as string)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"

# Example call (not in original but useful)
bill, message = generate_bill(3, 2)
print("Total bill:", bill)
print(message)
