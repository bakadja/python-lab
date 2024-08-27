
def bubble_sort(list):
    """basic bubble sort algorithm"""
    n = len(list)

    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list


#call the funktion
list = [1,10,7,5,9,4,6,3,8,2]
sorted_list = bubble_sort(list)

print(sorted_list)