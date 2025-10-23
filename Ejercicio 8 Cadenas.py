precio = (input("Cuanto vale el producto?:"))

var= precio.split(".")
euros = var[0]
centimos = var[1]

print ("Tienes",euros,"euros")
print ("Tienes",centimos,"centimos")