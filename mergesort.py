

def mergesort(arr):
    if len(arr) > 1:

        leftarr = arr[:len(arr)//2]
        rightarr = arr[len(arr)//2:]



    # recusion
        mergesort(leftarr)
        mergesort(rightarr) 

        i = 0
        j = 0 
        k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1

            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1
    
        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1



# arrtest = [8,9,4,5,7,6,2]
# mergesort(arrtest)
# print(arrtest)



user_input = input("Enter space-separated values: ")
array = list(map(int, user_input.split()))
mergesort(array)
print(array)