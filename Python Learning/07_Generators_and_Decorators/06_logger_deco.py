from functools import wraps


# Ye decorator function call hone se pehle aur baad me
# activity log karta hai.

def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # func.__name__ se function ka actual name milta hai.
        print(f"Calling: {func.__name__}")

        # *args -> positional arguments
        # **kwargs -> keyword arguments
        result = func(*args, **kwargs)

        print(f"Finished: {func.__name__}")

        return result

    return wrapper


@log_activity
def brew_chai(chai_type, milk="no"):
    print(f"Brewing {chai_type} chai and milk status: {milk}")


brew_chai("Masala")
brew_chai("Ginger", milk="yes")