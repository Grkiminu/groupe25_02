mots = input("Entrez des mots séparés par des espaces : ").split()  
voyelles = "aeiouyAEIOUY"  
total_voyelles = 0  

for mot in mots:  
    for lettre in mot:  
        if lettre in voyelles:  
            total_voyelles += 1  

print(f"Nombre total de voyelles : {total_voyelles}")

q = input("Cliquez sur ENTER pour quitter..")
