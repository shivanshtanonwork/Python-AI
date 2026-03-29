favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
    ]

# find unique chais we convert it to Set
unique_chais = {chai for chai in favourite_chais}

print(unique_chais)

recipes = {
    "Masala Chai" : ["ginger", "cardamon", "clove"],
    "Elaichi Chai" : ["milk", "cardmon", "elaichi"],
    "Spicy Chai" : ["ginger", "pepper", "clove"],
}

# find unique spices
unique_spices = {spice for ingrediants in recipes.values() for spice in ingrediants}

print(unique_spices)