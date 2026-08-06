
class ChaiCup:
    size = 150  

    def describe(self):
        return f"A {self.size}ml chai cup"

cup = ChaiCup()

#Automatically self
print(cup.describe())

# Class ke through call karte timw object manually dena padta hai.
print(ChaiCup.describe(cup))

cup_two = ChaiCup()
cup_two.size = 100
print(cup_two.describe())


class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"

# Object create hote hi __init__ automatically call hota hai.
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())
