def calcular(a, b, op):  
    if op == "+":  
        return a + b  
    elif op == "-":  
        return a - b  
    elif op == "*":  
        return a * b  
    elif op == "/":  
        if b != 0:  
            return a / b  
        else:  
            return "Division par zéro impossible."  
    else:  
        return "Opérateur non valide."  


# Exemple d'utilisation  
x = float(input("Nombre 1 : "))  
y = float(input("Nombre 2 : "))  
operation = input("Opération (+, -, *, /) : ")  
resultat = calcular(x, y, operation)  
print(f"Résultat : {resultat}") 

q = input("Cliquez sur ENTER pour quitter..")
