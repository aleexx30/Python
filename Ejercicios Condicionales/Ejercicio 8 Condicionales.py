
puntuacion = float(input("Cual es tu puntiacion?:"))
ganancia=2400

if puntuacion == 0.0:
    total=ganancia*puntuacion
    print("Tu rendimineto es inaceptable,recibes ", total , "euros.")
elif puntuacion == 0.4:
    total=ganancia*puntuacion
    print("Tu rendimineto es aceptable,recibes ", total , "euros.")
elif puntuacion >= 0.6:
    total=ganancia*puntuacion
    print("Tu rendimineto es meritorio,recibes", total , "euros.")
else:
    print("Introduce un puntuacion valida.")
