# Problem:
# Ek tea stall me digital token display hai.
# Har customer ko ek token number milta hai, 
# jo 1 se 10 tak hota hai.
# Hume for loop use karke ye display karwana hai.

# range(1, 11) => 1 se 10 tak numbers (11 exclusive)
for token in range(1, 11):
    # f-string ka use - variable ko string me embed karne ke liye
    print(f"Serving chai to token #{token}")

