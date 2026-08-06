# Problem:
# Local cafe ka ek chhota sa program banana hai jo customer ko snack suggestion de.
# Agar user 'cookies' ya 'samosa' bole toh order confirm ho.
# Agar koi aur bole toh batao ki sirf yahi snacks available hain.

# Step 1: Take snack input from user
# input() se string milegi, isliye lowercase (.lower()) me convert karenge
# Taaki "Cookies", "cookies", "COOKIEs" sab ek jaise treat ho.
snack = input("Enter your preferred snack (cookies/samosa): ").lower()

# Step 2: Check if snack available
# if condition + 'or' operator ka use karke 'cookies' ya 'samosa' match karenge.
if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}.")
else:
    print("Sorry, we only serve cookies or samosa.")

