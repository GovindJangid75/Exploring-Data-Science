# Problem statement: 
# Functions can return values which can be stored and used later. 
# Agar function mein return statement nahi hai, to by default woh None return karta hai.
# Also dekhte hain kaise function multiple values return karta hai aur unhe unpack karte hain.

# Simple function jo kuch print karta hai aur koi value return nahi karta
def make_chai():
    # return "Here is your masala chai"
    print("Here is your masala chai")

return_value = make_chai()  # Function call
print(return_value)  # Output hoga None kyunki function ne kuch return nahi kiya

# Function with pass statement - basically empty function
def idle_chaiwala():
    pass

print(idle_chaiwala())  # Iska output bhi None hoga

# Function jo ek value return karta hai
def sold_cups():
    return 120

total = sold_cups()  # Return value ko variable mein store kar rahe hain
print(total)  # Output: 120

# Function jo conditionally return karta hai
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("chai")  # Yeh line kabhi execute nahi hogi kyunki return ke baad nahi jaata

print(chai_status(0))  # Output: Sorry, chai over
print(chai_status(5))  # Output: Chai is ready

# Function jo multiple values return karta hai (tuple form mein)
def chai_report():
    return 100, 20, 10  # sold, remaining, not_paid

sold, remaining, not_paid = chai_report()  # Multiple return values unpack kar rahe hain
print("Sold: ", sold)
print("Remaining: ", remaining)
