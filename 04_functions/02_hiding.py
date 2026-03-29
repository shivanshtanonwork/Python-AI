def get_input():
    print("Getting user input")

def validating_input():
    print("Validating user info")

def save_to_db():
    print("saving to db")

def register_user():
    get_input()
    validating_input()
    save_to_db()
    print("user registration complete")

register_user()


def calculate_bill(cups, price_of_cup):
    return cups * price_of_cup

cups = [1,2,3,4,5]

for cup in cups:
    final_amount = calculate_bill(cup,25)
    print(final_amount)


def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")

chai_type = "Lemon"
serve_chai()
print(f"Outside function : {chai_type}")


def chai_counter():
    chai_order = "Lemon" #enclosing scope

    def print_order():
        chai_order = "ginger"
        print("Inner : ", chai_order)
    print_order()
    print('Outer : ', chai_order)

chai_order = "Tulsi" # global scope
chai_counter()
print("Global : ", chai_order)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai(tea="Green", milk="No", sugar="No")

# args *kwargs - key value arguments
def speacial_chai(*ingreadiants, **extras):
    print("ingreadiants", ingreadiants)
    print("extras", extras)

speacial_chai("Cinnamon", "Cardmon", sweetener="Honey", foam="yes")


# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()