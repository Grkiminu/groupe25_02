livres = [
    {"titre": "Python debutant", "auteur": "Dupont", "annee": 2008},
    {"titre": "Maitriser Python", "auteur": "Dupont", "annee": 2015},
    {"titre": "Python avancé", "auteur": "Dupont", "annee": 2021}
]

print("Livres publiés après 2010 :")
for livre in livres:
    if livre["annee"] > 2010:
        print(f"{livre['titre']} ({livre['annee']}) - {livre['auteur']}")

q = input("Appuyez sur ENTER pour quitter..")
