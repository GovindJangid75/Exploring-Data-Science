
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    # Getter
    @property
    def age(self):
        # leaf.age 
        return self._age + 2

    # Setter
    @age.setter
    def age(self, age):
        # Value set hone se pehle validation.
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError(
                "Tea leaf age must be between 1 and 5 years"
            )


leaf = TeaLeaf(2)

# Getter
print(leaf.age)

# Setter
leaf.age = 4
print(leaf.age)

# Invalid value -> ValueError
# leaf.age = 6
