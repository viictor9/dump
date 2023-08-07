import timeit

def bubble(arr):
    n = len(arr) - 1

    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, n):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr



def merge(a):
    return a 


def insertion(a):
    x_length = range(1, len(a))
    for i in x_length:
        toSort = a[i] 

        while a[i-1] > toSort and i > 0:
            a[i], a[i-1] = a[i-1], a[i]
            i = i -1

    return a
    

def selection(a):

    indexing_length = range(0, len(a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(a)):
            if a[j] < a[min_value]:
                min_value = j


        if min_value != i:
            a[min_value], a[i] = a[i], a[min_value]

    return a


choose = int(input("Enter your choice in number\n1:Bubble \n2:Merge \n3:Insertion \n4:Selection \n"))
values = input("enter values seperated by space: ")
array = list(map(int, values.split()))

if choose == 1:
    print("unsorted : ", array)
    print("sorted : ", bubble(array))
    timetaken = timeit.timeit(lambda: bubble(array), number=1)
    print("time taken to perform is ", timetaken, "seconds")

elif choose == 2:
    print("unsorted : ", array)
    print("sorted : ", merge(array))
    timetaken = timeit.timeit(lambda: merge(array), number=1)
    print("time taken to perform is ", timetaken, "seconds")

elif choose == 3:
    print("unsorted : ", array)
    print("sorted : ", insertion(array))
    timetaken = timeit.timeit(lambda: insertion(array), number=1)
    print("time taken to perform is ", timetaken, "seconds")

else:
    print("unsorted : ", array)
    print("sorted : ", selection(array))
    timetaken = timeit.timeit(lambda: selection(array), number=1)
    print("time taken to perform is ", timetaken, "seconds")