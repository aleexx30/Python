num1=int(input("Dime un numero:"))
num2=int(input("Dime un numero:"))

if num1%num2!=0:
    resto=str(num1%num2)
    print("El resto es "+resto)
else:
    print("Error")