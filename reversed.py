'''
2-  Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
'''
def reversed(lst):
    lst = lst[::-1]
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    return lst

# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[7, 6, 5], [4, 3], [2, 1]]

