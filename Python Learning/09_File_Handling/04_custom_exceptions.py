# Custom Exceptions in Python

# Custom exception -> apna khud ka error

class OutOfIngredientsError(Exception):
    pass


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError(
            "Milk Or sugar to le aa Uncle, chai kiski bnau?"
        )

    print("Chai is ready... pee le ab")


make_chai(1, 1)

# OutOfIngredientsError
# make_chai(0, 1)