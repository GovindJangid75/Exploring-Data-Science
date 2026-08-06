# fun with exceptions or erros 

class InvalidChaiError(Exception):
    pass


def bill(flavor, cups):
    menu = {
        "masala": 20,
        "ginger": 40
    }

    try:
        if flavor not in menu:
            raise InvalidChaiError(
                "Bhai menu me likha hai ache se, ye chai nahi milti"
            )

        if not isinstance(cups, int):
            raise TypeError(
                "Cups number me bata bhai, maths weak hai kya?"
            )

        total = menu[flavor] * cups
        print(f"{cups} cups of {flavor} chai = Rs.{total}")

    # Custom error
    except InvalidChaiError as e:
        print("Chai Error:", e)

    # Wrong data type
    except TypeError as e:
        print("Type Error:", e)

    # Other errors
    except Exception as e:
        print("Unexpected Error:", e)

    # Always runs
    finally:
        print("Thank you for visiting ChaiCode!")


bill("mint", 2)

print()

bill("masala", "three")

print()

bill("ginger", 3)