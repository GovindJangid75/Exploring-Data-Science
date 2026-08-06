# Problem:
# Agar order amount > 300 => delivery free (0 rupees)
# Warna => delivery charge 30 rupees.
# Yeh ek line me ternary operator se solve karna hai.

# Step 1: Take order amount and convert to integer
order_amount = int(input("Enter the order amount: "))

# Step 2: Calculate delivery fee using ternary operator
delivery_fee = 0 if order_amount > 300 else 30

# Step 3: Output fee
print(f"Delivery fees is {delivery_fee} rupees")
