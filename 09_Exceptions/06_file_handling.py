# file = open("order.txt", "w")
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close()

# new way

with open("order.txt", "w") as file:
    file.write("Ginger tea - 4cups")