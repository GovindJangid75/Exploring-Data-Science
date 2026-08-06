# Yeh ek function define kar raha hai jiska naam hai print_order
# Is function ke do inputs hain: name (aadmi ka naam) aur chai_type (chai ka type)
def print_order(name, chai_type):
    # Function ke andar yeh print karta hai ki kisne kaunsi chai order ki
    print(f"{name} orderded {chai_type} chai!")

# Function ko 3 baar call kiya gaya alag-alag naam aur chai type ke saath
print_order("Aman", "masala")    # Aman ne masala chai order ki
print_order("Hitesh", "Ginger")  # Hitesh ne Ginger chai order ki
print_order("Jia", "Tulsi")      # Jia ne Tulsi chai order ki
