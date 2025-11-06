nombre= str(input("como te llamas? :"))
nombre=nombre.capitalize()
sexo= str(input("Cual es tu sexo?:"))
sexo=sexo.capitalize()

if nombre[0] < "M" and sexo[0] == "M" or nombre[0] > "N" and sexo[0] == "H":
    print("Estas en el grupo A.")
else:
    print("Esta en el grupo B.")