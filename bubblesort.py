import timeit



def bubblesort(arr):
    
    n = len(arr) - 1

    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, n):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


a = input("enter values: ")
array = list(map(int, a.split()))


bubblesort(array)
print("sorted array", array)

timetaken = timeit.timeit(lambda: bubblesort(array), number=1)

print(timetaken)