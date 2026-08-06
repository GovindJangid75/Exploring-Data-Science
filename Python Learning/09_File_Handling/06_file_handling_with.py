# File Handling with try/finally and with

# Old way - file manually close karni padti hai

file = open("order.txt", "w")

try:
    file.write("Masala chai - 2 cups")
finally:
    file.close()


# Better way - using with
# with -> automatically close

with open("order.txt", "w") as file:
    file.write("Ginger tea - 7 cups")

print("Order save ho gaya bhai, tension na le ")


# Reading the file

with open("order.txt", "r") as file:
    order = file.read()

print("Saved order:", order)