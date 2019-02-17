import sys
import time

# ex_path = sys.argv[1] # Path de l'exemplaire
# find max value and store data in memory
def get_data(ex_path):
    data = []
    with open(ex_path) as f:
        for line in f: 
            value = [int(x) for x in line.split()][0]
            data.append(value)
    return data        

def get_max(data):
    max = 0
    for i in data:
        if max < int(i):
            max = int(i)
    return max     

# feed the index array
def set_index(data, max):
    index = [0] * (max + 1)
    for i in data:
        index[int(i)] += 1
    return index

#apply counting sort algo
def counting_sort_data(data, max) :
    index = set_index(data, max)
    sorted_data = []
    for i, value in enumerate(index):
        if value != 0:
            for j in range(0, value): 
                sorted_data.append(i)
    return sorted_data

def run():
    ex_path = sys.argv[1] # Path de l'exemplaire
    ex_path_temp = ex_path
    times = []

    for i in range(0, 29):
        ex_path = ex_path_temp + "_" + str(i) + ".txt"
        data = get_data(ex_path)
        max = get_max(data)
        
        start = time.time()
        sorted_values = counting_sort_data(data, max)
        end = time.time()

        options = sys.argv[2:]

        if '-p' in options: # On imprime les nombres triés    
            print("sorted_values")
                    
        if '-t' in options: # On imprime le temps d'exécution
            time_ = end - start
            times.append(time_)
            # print(end - start) # Données bidon, mais output du bon format demandé

    average_time = sum(times) / len(times)
    print(average_time)

if __name__ == '__main__':
    run()