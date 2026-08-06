

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class ElachiChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # Parent class ka __init__ call hoga.
        # self manually pass karne ki need nahi hai.
        super().__init__(type_, strength)
        self.spice_level = spice_level


Elachi = ElachiChai("Elachi", "Strong", "High")

print(Elachi.type)
print(Elachi.strength)
print(Elachi.spice_level)


# Avoid code duplication:
# self.type = type_
# self.strength = strength

# Possible:
# Chai.__init__(self, type_, strength)

# Preferred:
# super().__init__(type_, strength)
