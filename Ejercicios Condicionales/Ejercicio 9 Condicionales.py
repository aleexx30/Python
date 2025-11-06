
edad= int(input("Cuantos años tienes?:"))

if edad < 4 :
    print("Puedes entrar gratis.")
elif edad >= 4 and edad < 18 :
    print("Tienes que pagar 5€")
else:
    print("Tienes que pagar 10€")
