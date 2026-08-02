# Chapter 7: Tuples and Membership Testing

# Tuple kya hota hai?
# Tuple ek aisa data container hai jo multiple values ko ek saath rakhta hai, 
# aur ye immutable hota hai matlab ki aap isme values change nahi kar sakte.
# Tuple ko hum round brackets () ke andar values daal kar banate hain.

masala_spices = ("cardamom", "clove", "cinnamon")
print("Masala spices:", masala_spices)  # Tuple print karenge

# Tuple unpacking ka matlab hota hai ki tuple ke andar jitne elements hain,
# unn sab ko hum alag variables me ek saath assign kar sakte hain.
spice_one, spice_two, spice_three = masala_spices
print("Spice One:", spice_one)   # cardamom
print("Spice Two:", spice_two)   # clove
print("Spice Three:", spice_three)  # cinnamon

# Hum ek aur tuple bana sakte hain jaise yeh ratios ke liye.
# Yaha humne ginger aur cardamom ka ratio define kiya hai.
ginger_ratio, cardamom_ratio = (2, 1)
print(f"Ginger ratio: {ginger_ratio}")       # Output: 2
print(f"Cardamom ratio: {cardamom_ratio}")   # Output: 1

# Python me ek special feature hai jise hum swapping kehte hain.
# Bina intermediate variable ke hum do variables ki values swap kar sakte hain.
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print("After swapping:")
print(f"Ginger ratio: {ginger_ratio}")       # Output: 1
print(f"Cardamom ratio: {cardamom_ratio}")   # Output: 2

# Membership testing: 'in' keyword ka use kar ke hum check kar sakte hain

# ki koi value tuple ke andar maujood hai ya nahi.
print("Is 'ginger' in masala_spices?", "ginger" in masala_spices)    # False, kyunki ginger tuple me nahi hai
print("Is 'cinnamon' in masala_spices?", "cinnamon" in masala_spices) # True, cinnamon tuple me hai
print("Is 'Cinnamon' in masala_spices?", "Cinnamon" in masala_spices) # False, case sensitive check hota hai

