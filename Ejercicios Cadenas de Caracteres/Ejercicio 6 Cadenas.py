frase= str(input("Introduce una frase:"))
vocal= str(input("Introduce una vocal:"))

frase_modificada = frase.replace(vocal, vocal.upper())


print(frase_modificada)