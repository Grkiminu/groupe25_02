while True:  
    try:  
        n = int(input("Entrez un entier positif : "))  
        if n < 0:  
            raise ValueError("Nombre négatif interdit.")  
        break  
    except ValueError as e:  
        print(f"Erreur : {e}")  

print(f"Vous avez saisi : {n}") 

q = input("Appuyer sur ENTER pour quitter..")
