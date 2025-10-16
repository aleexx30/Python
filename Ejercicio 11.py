

banco= float(input(("Cuanto dinero vas a meter en el banco?")))

Año1= round(float(banco*(1+0.04)),2)
Año2= round(float(Año1*(1+0.04)),2)
Año3= round(float(Año2*(1+0.04)),2)

print("El año 1 tendras:",Año1,"El año dos tendras:",Año2,"Y el año 3 tendras",Año3)