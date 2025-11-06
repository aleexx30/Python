
pizza = str(input("Quieres una pizza vegetariana o normal?.:"))

pizza=pizza.lower()


if pizza == "vegetariana":
        print("La pizza vegetariana tiene Pimiento o tofu.")
        ingred = str(input("Que ingrediente quieres?"))

elif pizza == "normal":
        print("La pizza normal tiene Peperoni , jamon y salmon")
        ingred = str(input("Que ingrediente quieres?"))

print ("Has escogido la pizza", pizza , ",que lleva tomate,mozarella y", ingred ,)
