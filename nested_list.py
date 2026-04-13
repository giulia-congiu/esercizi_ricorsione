def count_leaf_nodes(input_list):
    if len(input_list) == 0:
        return 0    #se la lista è vuota ridai 0
    else:
        counter = 0
        for element in input_list:
            #per ogni elemento della lista vedo se è una lista o meno
            if type(element) == list:
                #if it is a list, we count it's element with a recursion
                counter += count_leaf_nodes(element)
                #else we add +1
            else: #se non è una lista
                counter += 1
        return counter

if __name__ == '__main__':
    names = ['Adam', ['Bob', ['Mike', 'Cat'], 'Barb', 'Bert'],'Alex', ['Bea', 'Bill'], 'Ann']
    print(f'Gli elementi totali nella lista sono {count_leaf_nodes(names)}')
