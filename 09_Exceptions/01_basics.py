# chai_menu = {"masala": 30, "ginger": 40}

# try:
#     chai_menu["elaichi"]
# except KeyError:
#     print("The key you are trying to accept does not exists")

# print("Hello Chai")

def serve_chai(flavour):
    try:
        print("Preparing chai")
        if flavour == "unknown":
            raise ValueError("We dont know that flavour")
    except ValueError as e:
        print("Error :", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next customer please")

serve_chai("Masalaa")
serve_chai("unknown")