def brew_chai(flavor):
    if flavor not in ["masalal", "ginger", "elaichi"]:
        raise ValueError("Unsupported chai")
    print(f"brewing {flavor} chai.")

brew_chai("ginger")