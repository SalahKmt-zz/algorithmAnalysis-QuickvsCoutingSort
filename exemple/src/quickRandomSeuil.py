import sys

ex_path = sys.argv[1] # Path de l'exemplaire

# create the index
data = []

# store data in memory
with open(ex_path) as f:
    for line in f: 
        data.append([int(x) for x in line.split()][0])

options = sys.argv[2:]

if '-p' in options: # On imprime les nombres triés    
    print("sorted values here")
             
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé