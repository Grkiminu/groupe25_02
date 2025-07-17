nom_fichier = input("Nom du fichier à lire : ")  

try:  
    with open(nom_fichier, "r", encoding="utf-8") as f:  
        contenu = f.read()  
except FileNotFoundError:  
    print("Erreur : Fichier introuvable.")  
else:  
    print("Contenu du fichier :")  
    print(contenu) 

q = input("Appuyer sur ENTER pour quitter..")
