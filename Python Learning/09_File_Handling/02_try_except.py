

chai_menu = {
    "masala": 30,
    "ginger": 40
}

# try -> code jisme error aa sakta hai
# except -> error ko handle karta hai

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key does not exist")

print("Hello ChaiCode")



def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")

        if flavor == "unknown":
            raise ValueError("We don't know that flavor")

    except ValueError as e:
        print("Error:", e)

    # else
    else:
        print(f"{flavor} chai is served")

    # finally
    finally:
        print("Next customer please")


serve_chai("masala")
serve_chai("unknown")