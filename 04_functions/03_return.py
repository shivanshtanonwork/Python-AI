# def make_chai():
#     # return "Here is your masala chai"
#     print("Here is you chai")

# returned_value = make_chai()
# print(returned_value)


def ideal_chaiwala():
    pass

print(ideal_chaiwala())

# return one value
def sold_cups():
    return 120

total = sold_cups()
print(total)

# return early from a function
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))

#return multiple value
def chai_report():
    return 100, 20  #sold, remaining

sold, remaining = chai_report()
print("Sold", sold)
print("Remaining", remaining)