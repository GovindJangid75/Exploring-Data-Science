# Yahan pe 'yield from' use hua hai do generators ko merge karne ke liye -- ek full chai menu mil jaata hai.
# local_chai aur imported_chai alag chai types deta hai, full_menu sab mila ke deta hai.
# chai_stall generator ko band karne par cleanup message print hota hai.

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.close()  #cleanup
