# Problem statement:
# 1. Functions can return values which can be stored and used.
# 2. Using global variables to track state inside functions is generally not recommended because it makes code hard to debug.
# 3. Recursion example in pour_chai function.
# 4. Using filter and lambda for list comprehension style filtering.

# Function jo cups ke hisaab se total chai quantify karta hai
def pure_chai(cups):
    return cups * 10  # Har cup ke liye 10 units chai

total_chai = 0  # Global variable jo pure nahi hai but dikhane ke liye use kiya

# Recommended nahi, global variable ko function ke andar modify kar rahe hain
def impure_chai(cups):
    global total_chai
    total_chai += cups  # Global variable ko update kar raha hai

# Recursive function jo n se start kar ke 0 tak count karta hai aur value print karta hai
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)  # Recursion - function apne aap ko call karta hai n-1 ke saath

print(pour_chai(3))


# List of chai types
chai_types = ["light", "kadak", "ginger", "kadak"]

# Filter use karke "kadak" wala chai hata diya, baki sab strong chai hain
strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))

print(strong_chai)
