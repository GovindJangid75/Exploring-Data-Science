# Local scope example
def serve_chai():
    chai_type = "Masala"  # yeh variable sirf is function ke andar hi accessible hai (local scope)
    print(f"Inside function {chai_type}")

chai_type = "Lemon"  # yeh variable global scope mein hai
serve_chai()  # function call karein
print(f"Outside function: {chai_type}")  # global chai_type print hoga

# Enclosing scope example (nested functions)
def chai_counter():
    chai_order = "lemon"  # yeh enclosing scope ka variable hai
    
    def print_order():
        chai_order = "Ginger"  # yeh print_order function ka local variable hai
        print("Inner:", chai_order)  # inner local variable print karega
    
    print_order()  # inner function ko call karte hain
    print("Outer: ", chai_order)  # enclosing variable print karega

chai_order = "Tulsi"  # global variable
chai_counter()  # function call karte hain
print("Global :", chai_order)  # global variable print hoga
