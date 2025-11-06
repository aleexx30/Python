

renta=int(input("Cual es tu renta anual?:"))



if renta < 10000:
    renta=renta*0.95
    print("Te corresponde ", renta , "euros")
elif renta >= 10000 and renta < 20000 :
    renta=renta*0.85
    print("Te corresponde ", renta , "euros")
elif renta >= 20000 and renta < 35000 :
    renta=renta*0.80
    print("Te corresponde ", renta , "euros")
elif renta >= 35000 and renta < 60000 :
    renta=renta*0.70
    print("Te corresponde ", renta , "euros")
elif renta >= 60000:
    renta=renta*0.60
    print("Te corresponde ", renta , "euros")



