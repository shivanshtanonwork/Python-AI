class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)
 
#creating objects from class chai
masala = Chai()
print(f"Masala : {masala.origin}")
print(masala.is_hot)