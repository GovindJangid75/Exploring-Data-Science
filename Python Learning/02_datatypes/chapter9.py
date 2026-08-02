# Chapter 9: Set and Frozenset in Python (with Hinglish Explanation)

# Set kya hota hai?
# Set ek unordered collection hota hai jisme har element unique hota hai.
# Sets ko hum curly braces {} ke andar define karte hain.

# Essential spices ka set
essential_spices = {"cardamom", "ginger", "cinnamon"}

# Optional spices ka set
optional_spices = {"cloves", "ginger", "black pepper", "cinnamon"}

print("Essential spices:", essential_spices)
print("Optional spices:", optional_spices)

# 1. Set Union - dono sets ke unique elements ka milap (duplicate nahi aayega)
all_spices = essential_spices | optional_spices  # Pipe '|' operator se union hota hai
print("All spices (Union):", all_spices)

# 2. Set Intersection - dono sets me jo common element hai
common_spices = essential_spices & optional_spices  # Ampersand '&' operator se intersection hota hai
print("Common spices (Intersection):", common_spices)

# 3. Set Difference - pehle set me jo hain but dusre set me nahi
only_in_essential = essential_spices - optional_spices
print("Only in essential spices (Difference):", only_in_essential)

# 4. Membership Testing - check karo element set me hai ya nahi
print("Is 'cloves' in essential_spices?", "cloves" in essential_spices)
print("Is 'cloves' in optional_spices?", "cloves" in optional_spices)

# 5. Frozenset - immutable set (elements badal nahi sakte)
frozen_essential = frozenset(essential_spices)
print("Frozen essential spices:", frozen_essential)

# Example: Frozenset me koi add/remove nahi kar sakte
# frozen_essential.add("turmeric")  # Error aayega (immutable hai)

