from functools import wraps


# Decorator ek function ko wrap karta hai aur
# original function ko change kiye bina extra functionality add karta hai.

def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("Before function runs")

        func()

        print("After function runs")

    return wrapper


@my_decorator
def greet():
    print("Hello from decorators class from ChaiCode")


greet()

# @wraps(func) original function ka metadata preserve karta hai.
# Isliye yaha "greet" print hoga, "wrapper" nahi.
print(greet.__name__)