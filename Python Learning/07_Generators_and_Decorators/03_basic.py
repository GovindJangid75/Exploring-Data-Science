# Yahaan pe .send() ka use dikhaya gaya hai generator ke saath.
# chai_customer pehle welcome karta hai, uske baad user order bhej sakta hai send se.
# Jaise send("Masala Chai") se woh chai bana raha hai, send("Lemon Chai") se doosri.

def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall)  # start the generator
stall.send("Masala Chai")
stall.send("Lemon Chai")
