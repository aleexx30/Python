correoOriginal = str(input("Dime tu correo electronico:"))

usuario = str(correoOriginal[:correoOriginal.find("@")])

nuevoCorreo = usuario + "@ceu.es"

print ("Tu nuevo correo es ",nuevoCorreo)

