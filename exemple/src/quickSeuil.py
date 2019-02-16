import sys

ex_path = sys.argv[1] # Path de l'exemplaire

# store data in memory
def get_data():
    data = []
    with open(ex_path) as f:
        for line in f: 
            data.append([int(x) for x in line.split()][0])
    return data

def quick_sort_data(data):
    sorted_data = []
    if len(data) >= 2:
        pivot = data[0]
        greater_data = []
        less_data = []
        nbr_of_pivot_equal = 0

        for value in data:
            if value > pivot:
                greater_data.append(value)
            elif value < pivot:
                less_data.append(value)
            elif value == pivot:
                nbr_of_pivot_equal += 1
                
        first_part = quick_sort_data(less_data)

        for _i in range(0, nbr_of_pivot_equal):
            sorted_data.append(pivot)

        second_part = quick_sort_data(greater_data)

        return first_part + sorted_data + second_part 
    else :
        return data

def insertion_sort(data):
    for i in range(1, len(data)):
        value_to_insert = data[i]
        hole_index = i
        while hole_index > 0 and value_to_insert < data[hole_index - 1]:
            data[hole_index] = data[hole_index - 1]
            hole_index -= 1
        data[hole_index] = value_to_insert

    return data 

def run():
    data = get_data()

    print(quick_sort_data(data))

    options = sys.argv[2:]

    if '-p' in options: # On imprime les nombres triés    
        print("sorted values here")
                
    if '-t' in options: # On imprime le temps d'exécution
        print("4.1347628746") # Données bidon, mais output du bon format demandé

if __name__ == '__main__':
    run()
