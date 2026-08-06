# Yeh function hai calculate_bill jo total bill calculate karta hai
# Iske do inputs hain: cups (kitne cups chai), price_per_cup (ek cup ki keemat)
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup  # Cups aur price ko multiply karke total bill return karta hai

# Function ko call kar ke bill calculate kar rahe hain 3 cups aur 15 rupees per cup
my_bill = calculate_bill(3, 15)
print(my_bill)  # Output hoga 45

# Seedha print statement mein bhi function call karke table 2 ka order ka bill print kar rahe hain
print("Order for table 2: ", calculate_bill(2, 50))  # Output hoga "Order for table 2: 100"
