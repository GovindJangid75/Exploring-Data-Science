# Enumerate ka matlab hai ki list ke elements ke saath-saath unka index number bhi mile.
# Default index 0 se start hota hai, lekin hum start=1 dekar numbering change kar sakte hain.

menu = ["Green Chai", "Lemon Chai", "Spiced Chai", "Mint Chai"]

# enumerate(menu, start=1) => (index, item) pairs deta hai
for idx, item in enumerate(menu, start=1):
    print(f"{idx}. {item}")

