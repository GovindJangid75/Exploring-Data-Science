# Classes and Objects in Python

# Class ek blueprint/template hoti hai.
# Object us class ka actual instance hota hai.

class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

#object create
ginger_tea = Chai()

print(type(ginger_tea))

# Check kar rahe hain object kis class ka hai
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
