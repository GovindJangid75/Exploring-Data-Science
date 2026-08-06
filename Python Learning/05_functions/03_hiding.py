# Yeh function hai get_input jo user se input leta hai
def get_input():
    print("Getting user input")

# Yeh function hai validate_input jo user ke input ko validate karta hai
def validate_input():
    print("Validating the user info")

# Yeh function hai save_to_db jo data ko database mein save karta hai
def save_to_db():
    print("saving to database")

# Yeh function hai register_user jo pehle teeno functions ko call karta hai aur user registration complete karta hai
def register_user():
    get_input()            # User se input leta hai
    validate_input()       # Input ko validate karta hai
    save_to_db()           # Data ko database mein save karta hai
    print("User registration complete")  # Registration complete hone ka message print karta hai

# Function ko call kar rahe hain jisse pura user registration process chalega
register_user()