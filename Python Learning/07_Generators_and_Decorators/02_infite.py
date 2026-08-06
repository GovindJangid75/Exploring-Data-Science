# Yeh generator infinite hai. 'infinite_chai' har call pe next refill deta rahega, kabhi rukta nahi.
# Do alag-alag generator objects banaye gaye hain: 'refill' & 'user2'.
# refill se 5 chai milti hai, user2 se 6; 

def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))
