# Raising Errors using raise

# raise -> manually error generate 

def brew_chai(flavor):
    available_flavors = ["masala", "ginger", "elaichai"]

    if flavor not in available_flavors:
        raise ValueError("Unsupported chai flavor... Nhi mile ye chai tuje chala ja")

    print(f"Brewing {flavor} chai...")


brew_chai("masala")

# ValueError
# brew_chai("mint")