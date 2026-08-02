# Example: Immutable Objects in Python (Numbers)

# Pehle ek variable banate hain
sugar_amount = 2

# Print initial value
print(f"Initial sugar amount: {sugar_amount}")

# Change the variable value
sugar_amount = 12

# Print second value
print(f"Second sugar amount: {sugar_amount}")

# Check identity (memory address) of numbers
print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# OPTIONAL: Check identity of variable at each stage
a = 2
print(f"ID of a (with value 2): {id(a)}")

a = 12
print(f"ID of a (after changing to 12): {id(a)}")
