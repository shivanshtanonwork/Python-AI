orders = ["Shivansh", "Vidushi", "Tony"]

for name in orders:
    print(f"Order read for {name}")

menu = ["Green", "lemon", "spiced", "mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")


names = ["Shivansh", "Vidushi", "Aanvee"]
bill = [50, 70, 100]

for name, amount in zip(names, bill):
    print(f"name {name} : amount {amount}")