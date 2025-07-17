try:  
    a = float(input("Nombre 1 : "))  
    b = float(input("Nombre 2 : "))  
    result = a / b  
except ZeroDivisionError:  
    print("Erreur : Division par zéro !")  
else:  
    print(f"Résultat : {result}") 

q = input("Appuyer sur ENTER pour quitter..")
