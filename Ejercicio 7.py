
Altura = float(input(("Cuanto mides en metros?: ")))
Peso = float(input(("Cuanto pesas en kg?: ")))


imc = float(((Peso)/(Altura**2)))
redondeado= str(round(imc,2))

print ("Tu imc es : "+redondeado)