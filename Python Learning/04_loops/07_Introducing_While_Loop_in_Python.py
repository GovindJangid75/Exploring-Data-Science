# While loop ek condition ke true hone tak repeat hota hai.
# Example: Chai garam karna jab tak temperature 100°C na ho jaye.

temperature = 40  # Starting temp

while temperature < 100:  
    print(f"Current temperature: {temperature}°C")
    temperature += 15  # Har step me 15°C badhaye

print("Tea is ready to be served!")

# Output:
# Current temperature: 40°C
# Current temperature: 55°C
# Current temperature: 70°C
# Current temperature: 85°C
# Tea is ready to be served!
