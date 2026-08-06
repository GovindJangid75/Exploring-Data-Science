# Problem:
# Tea stall ke liye program jo cup size ke hisaab se price bataye:
# small: Rs.10, medium: Rs.15, large: Rs.20
# Aur agar galat size de toh "unknown cup size" likhe.

# Step 1: Take cup size input + lowercase conversion
cup = input("Choose your cup size (small/medium/large): ").lower()

# Step 2: Match size with price
if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")
