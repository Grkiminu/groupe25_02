entree = input("Entrez des elements : ")
liste = entree.split()

for i, elem in enumerate(liste):
    print(f"Indice {i} : {elem}")
        
q = input("Appuyez sur ENTER pour quitter..")
