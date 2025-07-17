# Demande d’informations à l’utilisateur  
prenom = input("Entrez votre prénom : ")  
age = int(input("Entrez votre âge : "))  
ville = input("Entrez votre ville : ")  
mettier = input("Entrez votre métier : ")

# Approximation des jours vécus  
jours_vécus = age * 365

# Affichage formaté  
print("\n== PROFIL UTILISATEUR ==")  
print(f"Prénom : {prenom}")
print(f"Age : {age} ans ({jours_vécus} jours vécus environ)")  
print(f"Ville : {ville}")  
print(f"Métier : {mettier}")

q=input("Cliquez sur ENTER pour quitter..")  
