'''
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
'''

def flatten(lst):
    flat_list = []
    for i in lst:
        if type(i) == list:
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    return flat_list

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]