texte = input("Entrez une chaîne : ")  
inverse = ""  

for char in texte:  
    inverse = char + inverse  

print(f"Chaîne inversée : {inverse}")

q = input("Cliquez sur ENTER pour quitter..")
