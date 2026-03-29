flavours = ["ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")
    
print(f"Out of loop")

staff = [("Shivansh", 27),("Vidushi", 26),("Aanvee", 5)]

for name,age in staff:
    if age >= 18:
        print(f"{name} is elligible")
else:
    print(f"No one is eligble to manage the staff")


