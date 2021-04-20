# recursive
def bubbleSort(array: [int]) -> [int]:
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            bubbleSort(array)
    return array
  
#________________________________________________________
  
# iterative
def bubbleSort(array):
    for l in range(1, len(array)):
        for i in range(len(array) - l):
            if array[i] > array[i + 1]:
                   array[i], array[i + 1] = array[i + 1], array[i]
    return array
  
print(bubbleSort([])) # []
print(bubbleSort([1])) # [1]
print(bubbleSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(bubbleSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]
