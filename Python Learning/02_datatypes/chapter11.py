# Chapter 11: Introduction to Advanced Data Types and Collections in Python

# Advanced data types kya hain?
# Ye Python ke basic types se aage ke data structures hote hain,
# jo complex data ko efficiently handle karne me madad karte hain.
# Ye Python ke andar built-in nahi hote, aapko "import" karna padta hai kisi module se, mostly "collections" module se.

# Kuch common advanced data types:
# 1. datetime - Date and time ke sath kaam karne ke liye
# 2. calendar - Calendar functionality
# 3. timedelta - Do time points ke beech duration calculate karna

# Example: datetime se current UTC time lena
import datetime
now_utc = datetime.datetime.utcnow()
print("Current UTC time:", now_utc)

# Third party modules bhi hotay hain jaise:
# - arrow (datetime ko aur simplify karne wala)
# - dateutil (advanced date manipulation ke liye)

# Collections module ke important types:
from collections import namedtuple

# Namedtuple kya hota hai?
# Yeh ek tuple hota hai jisme fields ke names bhi hote hain,
# isse aap tuple ko field names ke through access kar sakte ho.

# Example of namedtuple:
ChaiProfile = namedtuple('ChaiProfile', ['flavor', 'aroma', 'color'])
profile = ChaiProfile(flavor='masala', aroma='spicy', color='brown')

print("Chai Profile:", profile)
print("Flavor:", profile.flavor)
print("Aroma:", profile.aroma)
print("Color:", profile.color)
