# Common Errors in Python

# IndexError - index range ke bahar ho
orders = ["elaichi", "masala"]

print(orders[0])
print(orders[1])

# print(orders[2])  # IndexError


# KeyError - dictionary me key exist na kare
chai_menu = {
    "masala": 30,
    "ginger": 40
}

print(chai_menu["masala"])

# print(chai_menu["elaichi"])  # KeyError


# ZeroDivisionError
# print(10 / 0)


# TypeError 
# print("10" + 5)


# NameError
# print(customer_name)