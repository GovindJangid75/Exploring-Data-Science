# Problem:
# Device ka 'status' check karna (active/offline)
# Agar active hai toh temperature check karein.
# Temp > 35 => High temperature alert, else "Normal temperature".
# Agar device offline => "Device is offline".

# Step 1: Define device status and temperature (in real app yeh sensors se aayega)
device_status = "active";
temperature = 38;

# Step 2: Outer if - check device status
if device_status == "active":
    # Nested if - check temperature only if active
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")

