from functools import wraps


# Authorization decorator user ka role check karta hai.
# Sirf admin ko protected function access karne dega.

def require_admin(func):

    @wraps(func)
    def wrapper(user_role):

        if user_role != "admin":
            print("Access denied: Admins only")
            return None

        return func(user_role)

    return wrapper


@require_admin
def access_tea_inventory(role):
    print("Access granted to tea inventory")


# Normal user ko access nahi milega.
access_tea_inventory("user")

# Admin ko access mil jayega.
access_tea_inventory("admin")