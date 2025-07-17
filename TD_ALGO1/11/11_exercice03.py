def est_palindrome(lemot):
    return lemot == lemot[::-1]


mot = input("Entrez un mot : ")

if est_palindrome(mot):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")

q = input("Cliquez sur ENTER pour quitter..")
