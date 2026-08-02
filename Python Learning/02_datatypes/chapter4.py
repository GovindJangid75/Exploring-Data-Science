# Chapter 4 - Booleans

# Boolean variable
is_boiling = True
stir_count = 5

# True counts as 1 when added
total_actions = stir_count + is_boiling
print(f"Total actions: {total_actions}")

# bool() conversion examples
milk_present = 0
print(f"Is there milk? {bool(milk_present)}")

milk_present = 1
print(f"Is there milk? {bool(milk_present)}")

milk_present = 11
print(f"Is there milk? {bool(milk_present)}")

milk_present = "Hitesh"
print(f"Is there milk? {bool(milk_present)}")

milk_present = None
print(f"Is there milk? {bool(milk_present)}")

# Logical Operators
water_hot = True
tea_added = False
can_serve_chai = water_hot and tea_added
print(f"Can serve chai? {can_serve_chai}")

tea_added = True
can_serve_chai = water_hot and tea_added
print(f"Can serve chai? {can_serve_chai}")

# Other operators (quick examples)
print(True or False)   # OR
print(not True)        # NOT
