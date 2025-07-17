carres = []  

for i in range(1, 21):  
    carres.append(i ** 2)  

print("Tous les carrés :", carres)  

print("Carrés > 100 :")  
for val in carres:  
    if val > 100:  
        print(val) 

q = input("Cliquez sur ENTER pour quitter..")
