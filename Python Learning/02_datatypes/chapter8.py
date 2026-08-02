# Chapter 8: List and String Operations in Python

# LIST BASICS - Mutable Data Type

# Ye list ek mutable sequence hai, matlab aap iske andar changes kar sakte ho, add, remove, update kar sakte ho
ingredients = ["water", "milk", "black tea"]  
print("Initial ingredients:", ingredients)  # Starting list print karte hain

# List me item add karna - append() method se last me add hota hai
ingredients.append("sugar")
print("After appending sugar:", ingredients)

# Specific position par item insert karna - insert(index, item)
ingredients.insert(1, "ginger")  # 1 index pe ginger insert kiya
print("After inserting ginger at position 1:", ingredients)

# Kisi item ko list se remove karna - remove(item)
ingredients.remove("water")
print("After removing water:", ingredients)

# Kisi index se item nikalo - pop() last se nikalta hai aur return bhi karta hai
last_item = ingredients.pop()
print("Popped last item:", last_item)
print("List after pop:", ingredients)

# List ko reverse karna - reverse() in-place reverse karta hai list ka order
ingredients.reverse()
print("List after reversing:", ingredients)

# List ko sort karna - sort() alphabetically/numerically sort karta hai list ko
ingredients.sort()
print("List after sorting:", ingredients)

# STRING OPERATIONS

# String immutable object hai, lekin bahut saare operations hum string pe kar sakte hain 
# String ko define karte hain
greeting = "Hello, World!"

# String length nikalna
print("Length of greeting:", len(greeting))

# Uppercase me convert karna
print("Uppercase:", greeting.upper())

# Lowercase me convert karna
print("Lowercase:", greeting.lower())

# String me koi substring hai ya nahi check karna using 'in'
print("Is 'World' in greeting?", 'World' in greeting)

# String ko split karna (space se by default)
words = greeting.split()
print("Split string into words:", words)

# String ko replace karna
new_greeting = greeting.replace("World", "Python")
print("Replaced string:", new_greeting)

# String ko reverse karna using slicing
reversed_greeting = greeting[::-1]
print("Reversed string:", reversed_greeting)

# String ko strip karna (leading and trailing spaces hataana)
spaced = "   hello   "
print("Before strip:", repr(spaced))
print("After strip:", repr(spaced.strip()))

# String join karna - list of strings ko ek string me join karna
joined = "-".join(words)
print("Joined words with hyphen:", joined)

# Check if string starts with or ends with certain substring
print("Starts with 'Hello':", greeting.startswith("Hello"))
print("Ends with '!':", greeting.endswith("!"))

# Count occurrence of a character or substring
count_l = greeting.count('l')
print("Count of 'l' in greeting:", count_l)

# String find - index of substring (-1 if not found)
index_world = greeting.find("World")
print("Index of 'World' in greeting:", index_world)





# Chapter: Operator Overloading and Bytearray in Python 

# Operator overloading kya hota hai?
# Wo concept jisme Python ke built-in operators (+, *, etc.) ko hum apne custom behavior ke liye use kar sakte hain.

# Example ke liye, humare paas base liquids ke lists hain:
water = ["water"]
milk = ["milk"]
extra_flavor = ["ginger"]

# Normal list ko plus operator se jodne ki koshish:
# Python automatically plus (+) ka use lists ko combine karne ke liye karta hai. 
liquid_mix = water + milk + extra_flavor
print("Liquid mix:", liquid_mix)
# Output: ['water', 'milk', 'ginger']
# Yaha pe plus operator ne lists ko concatenate kar diya. Ye hai operator overloading ka ek example.

# Dusra example - string multiplication:
strong_brew = "black tea " * 3
print("Strong brew (three times):", strong_brew)
# Output: black tea black tea black tea 
# Yaha string multiplication ka matlab hai string ko repeat karna.

# Agar hum list ko multiply karen:
water_milk = ["water", "milk"]
multi_liquid = water_milk * 3
print("Repeated liquid list:", multi_liquid)
# Output: ['water', 'milk', 'water', 'milk', 'water', 'milk']

# String ko list me convert karna:
spice = "cinnamon"
spice_list = list(spice)
print("String to list:", spice_list)
# Output: ['c', 'i', 'n', 'n', 'a', 'm', 'o', 'n']

# Bytearray kya hota hai?
# Ye ek mutable sequence hai integers ka (0-255 ke beech),
# which can be used to handle binary data efficiently.

raw_spice_data = bytearray(b"cinnamon")
print("Raw spice data (bytearray):", raw_spice_data)
# Output will be a bytearray representing "cinnamon"

# Bytearray me replace operation bhi kar sakte hain, but syntax thoda alag hota hai:
raw_spice_data = raw_spice_data.replace(b"cina", b"carda")
print("Replaced bytearray:", raw_spice_data)
# Output changes 'cina' to 'carda' in the bytearray

