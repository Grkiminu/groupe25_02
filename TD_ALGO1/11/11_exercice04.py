def convertir(usd):  
    eur = usd * 0.93  
    cfa = usd * 610  
    gbp = usd * 0.79  
    return eur, cfa, gbp  


montant = float(input("Montant en USD : "))  
meur, mcfa, mgbp = convertir(montant)

print(f"{montant} USD = {meur:.2f} EUR, {mcfa:.2f} CFA, {mgbp:.2f} GBP")

q = input("Cliquez sur ENTER pour quitter..")
