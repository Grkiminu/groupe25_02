mot = input("Entrez un mot (min. 5 lettres) : ")  

if len(mot) >= 5:  
    milieu = mot[2:-2]  
    print(f"Partie centrale : {milieu}")  
else:  
    print("Mot trop court.")

q = input("Appuyer la la touche ENTER pour quitter..")
