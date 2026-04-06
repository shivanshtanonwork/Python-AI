def process_order(item,quantity):
    try:
        if not isinstance(quantity, (int, float)):
            raise TypeError
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Qty must be in number")
    

process_order("masala",2)
process_order("masala","two")

