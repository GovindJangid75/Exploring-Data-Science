# Chapter 10: Dictionary in Python (with Hinglish Explanation)

# Dictionary kya hota hai?
# Dictionary ek mutable, unordered data structure hai jisme hum data ko key-value pairs me store karte hain.
# Ye list se alag hai kyunki isme indexing number se nahi balki unique keys se hoti hai.

# Dictionary banane ka example:
chai_order = {
    "type": "masala chai",
    "size": "large",
    "sugar": 2,
}


print("Initial chai order:", chai_order)

# Dictionary me naya data add karna:
chai_order["liquid"] = "milk"
print("After adding liquid:", chai_order)

# Kisi specific key ka value access karna:
print("Type of chai:", chai_order["type"])

# Dictionary se item remove karna using 'del':
del chai_order["liquid"]
print("After removing liquid:", chai_order)

# Membership test (check if key exists):
print("Is 'sugar' key present?", "sugar" in chai_order)
print("Is 'liquid' key present?", "liquid" in chai_order)

# Dictionary ke keys print karna:
print("All keys:", chai_order.keys())

# Dictionary ke values print karna:
print("All values: ", chai_order.values())

# Dictionary ke items (key-value pairs) print karna:
print("All items:", chai_order.items())

# Dictionary se item safely access karna using get() method:
# get() agar key nahi mile to default value return karta hai, crash nahi hone deta
customer_note = chai_order.get("customer_note", "No customer note provided")
print("Customer Note:", customer_note)

# Dictionary me value update karna:
chai_order["sugar"] = 1
print("After updating sugar:", chai_order)

# Kisi item ko pop karke remove karna aur value lena:
popped_value = chai_order.pop("sugar")
print("Popped sugar value:", popped_value)
print("After popping sugar:", chai_order)

