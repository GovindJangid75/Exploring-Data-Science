# Example: Mutable Objects in Python (Set)

# Start with empty set
spice_mix = set()

# Print initial spice mix and its ID
print(f"Initial spice mix: {spice_mix}")
print(f"Initial spice mix ID: {id(spice_mix)}")

# Add items to set
spice_mix.add("ginger")
spice_mix.add("cardamom")

# Print spice mix after adding spices
print(f"Spice mix after adding spices: {spice_mix}")
print(f"Spice mix ID after adding: {id(spice_mix)}")  # ID remains same

# Replace one spice (remove old, add new)
spice_mix.remove("cardamom")
spice_mix.add("lemon")

# Final spice mix
print(f"Final spice mix: {spice_mix}")
print(f"Final spice mix ID: {id(spice_mix)}")  # Still same as initial
