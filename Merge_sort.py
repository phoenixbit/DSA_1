# This program is designed to use merge sort algorithm to sort an array


def mergesort(array):
    # base case
    if len(array) > 1:
        split = len(array) // 2
        L = array[:split]
        M = array[split:]

        mergesort(L)
        mergesort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] > M[j]:
                array[k] = L[i]
                i += 1
                k += 1
            else:
                array[k] = M[j]
                j += 1
                k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array


def receive_array(array):
    input_data = int(input("Please enter the number of objects in the array : "))
    array = [0] * input_data
    print("Please enter the numbers one at a time. ")
    for i in range(input_data):
        array_input = int(input())
        array[i] = array_input
    return array


def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


base_array = []
if __name__ == '__main__':
    merge_array = receive_array(base_array)
    print("The array inputted is as follows : ")
    print_list(merge_array)
    merge_array = mergesort(merge_array)
    print("The sorted array is as follows : ")
    print_list(merge_array)
