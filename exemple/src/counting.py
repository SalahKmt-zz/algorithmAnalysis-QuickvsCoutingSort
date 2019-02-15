import sys

ex_path = sys.argv[1] # Path de l'exemplaire

# Algo ici
# create the index
data = open(ex_path, "r")
array = []
index = []
max = 0

# find max value and store data in memory
with open(ex_path) as f:
    for line in f: 
        value = [int(x) for x in line.split()][0]
        array.append(value)
        if max < value: 
            max = value

index = [0] * (max + 1)

# feed the index array
for i in data:
    index[int(i)] += 1

options = sys.argv[2:]

if '-p' in options: # On imprime les nombres triés    
    for i, value in enumerate(index):
        if value != 0:
            for j in range(1, value): 
                print(i, end=', ')
             
#if '-t' in options: # On imprime le temps d'exécution
    #print("4.1347628746") # Données bidon, mais output du bon format demandé
