# Problem statement: When you pass a mutable object like list to a function and modify it inside,
# the change reflects outside too because lists are passed by reference.
# Example: 
# chai = "Ginger chai"
# def prepare_chai(order):
#     print("Preparing ", order)
# prepare_chai(chai)
# print(chai)
# This works fine with string (immutable)

# But with list:
chai = [1, 2, 3]  # List jo mutable hai

def edit_chai(cup):
    cup[1] = 42  # List ke second element ko update kar rahe hain

edit_chai(chai)  # Function call karne par original list change ho jayegi
print(chai)  # Output: [1, 42, 3]

# Function with positional and keyword arguments example
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")  # Positional arguments
make_chai(tea="Green", sugar="Medium", milk="No")  # Keyword arguments

# Function with *args and **kwargs example
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)  # Tuple of positional extras
    print("Extras", extras)  # Dictionary of keyword extras

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")

# Problem with default mutable args and solution:
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []  # Nayi list create kar rahe hain taaki purani list modify na ho
    print(order)

chai_order()  # Output: []
chai_order()  # Output: []
