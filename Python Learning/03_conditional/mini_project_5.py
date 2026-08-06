
# Problem:
# Railway seat type ke hisaab se features show karo.
# Sleeper, AC, General, Luxury
# Aur agar invalid seat type ho toh "Invalid seat type" message.

# Step 1: Take seat type input (lowercase for matching)
seat_type = input("Enter seat type (sleeper/ac/general/luxury): ").lower()

# Step 2: match-case to map seat types
match seat_type:
    case "sleeper":
        print("No AC, beds available")
    case "ac":
        print("Air conditioned, comfy ride")
    case "general":
        print("Cheapest option, no reservation")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Invalid seat type")

