chai_type = "Plain"  # yeh global variable hai

def front_desk():
    def kitchen():
        global chai_type  # global keyword yeh batata hai ki chai_type global variable ko modify karna hai
        chai_type = "Irnai"  # global variable ko update kar diya
    
    kitchen()  # kitchen function call hota hai jo global chai_type ko change karta hai

front_desk()  # outer function call karte hain
print("Final global chai: ", chai_type)  # global variable print hota hai updated value ke sath
