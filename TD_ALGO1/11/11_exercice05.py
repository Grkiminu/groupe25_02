import random  
import string  


def generer_mdp(longueur):  
    caracteres = string.ascii_letters + string.digits  
    mdp = ''.join(random.choice(caracteres) for _ in range(longueur))  
    return mdp  


mlongueur = int(input("Longueur du mot de passe : "))
print(f"Mot de passe généré : {generer_mdp(mlongueur)}")

q = input("Cliquez sur ENTER pour quitter..")
