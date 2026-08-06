
class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    pass


cup = D()

print(cup.label)

# MRO = Method Resolution Order
# kis order me classes ke andar method search krna ye woh krna
print(D.__mro__)

# Is case me lookup:
# D -> C -> B -> A -> object
