
class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
       
        return [item.strip() for item in text.split(",")]


raw = " water , milk , ginger , honey "
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)


class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # Alternative constructor
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    # Another alternative constructor
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)


class SizeUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(SizeUtils.is_valid_size("Medium"))

order1 = ChaiOrder.from_dict({
    "tea_type": "Masala",
    "sweetness": "Medium",
    "size": "Large"
})

order2 = ChaiOrder.from_string("Ginger-Low-Small")

# Normal constructor
order3 = ChaiOrder("Masala", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)


# Instance Method -> self milta hai
# Class Method    -> @classmethod, cls milta hai
# Static Method   -> @staticmethod, self/cls nahi milta
# Static method ko self ya cls ki need nahi hoti.
