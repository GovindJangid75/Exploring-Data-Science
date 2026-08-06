# Yeh file do tareeke dikhata hai chai serve karne ke — ek normal function aur ek generator function.
# 'serve_chai' ek generator hai, jo baar baar 'yield' karke alag alag chai deta hai.
# 'get_chai_list' simple ek list return karta hai, bina generator ke.
# 'get_chai_gen' bhi generator hai, jo next() ke through ek-ek cup deta hai.
# Jab next(chai) teen baar call karte hain, three outputs milte hain.
# 4th baar call karne pe error aata hai kyunki generator finish ho chuka hai.

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()
# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai))  # gives error
