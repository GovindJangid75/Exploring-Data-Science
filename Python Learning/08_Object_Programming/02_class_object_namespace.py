#Attribute Shadowing

class Chai:
    origin = "India"

print(Chai.origin)

# Class banne ke baad bhi dynamically attribute add kar sakte hain.
Chai.is_hot = True
print(Chai.is_hot)

masala = Chai()

print(f"Masala origin: {masala.origin}")
print(f"Masala is hot: {masala.is_hot}")

masala.is_hot = False

print("Class:", Chai.is_hot)
print("Masala:", masala.is_hot)

# Individual object me new attribute 
masala.flavor = "Masala"
print(masala.flavor)


# Attribute Shadowing:--> 

class CuttingChai:
    temperature = "hot"
    strength = "Strong"

cutting = CuttingChai()
print(cutting.temperature)

# Instance attribute class attribute ko shadow karega.
cutting.temperature = "Mild"
cutting.cup = "small"

print("After changing:", cutting.temperature)
print("Cup size:", cutting.cup)
print("Class temperature:", CuttingChai.temperature)

# Instance attribute delete hone ke baad class value fallback hogi.
del cutting.temperature
print(cutting.temperature)

del cutting.cup

# Ye error dega, kyunki cup class me bhi nahi hai:
# print(cutting.cup)
