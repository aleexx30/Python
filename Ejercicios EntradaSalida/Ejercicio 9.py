Dinero= float(input("Cuanto dinero vas a invertir?:"))
Interes= float(input("Cual es el interes anual?:"))
Años= float(input("Durante cuantos años?:"))

Ganancia= Dinero*(1+Interes)**Años


print("Habras obtenido un total de:",Ganancia)