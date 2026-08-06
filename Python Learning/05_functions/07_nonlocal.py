chai_type = "ginger"  # yeh global variable nahi hai, bas function ke bahar defined hai

def update_order():
    chai_type = "Elaichi"  # yeh enclosing function ka variable hai (local to update_order)
    
    def kitchen():
        nonlocal chai_type  # nonlocal keyword batata hai ki yeh chai_type enclosing function (update_order) ka hai, na ki local
        chai_type = "Kesar" # isliye yeh kitchen function ke andar ham enclosing scope ke chai_type ko update kar rahe hain
    
    kitchen()  # kitchen function call karte hain jo chai_type ko "Kesar" se update karega
    print("After kitchen update", chai_type)  # yeh print karega updated value "Kesar"

update_order()
