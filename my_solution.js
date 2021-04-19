function bubbleSort(array) {
    for(let i = 0; i < array.length; i++){
        if(array[i] >  array[i+1]){
            // swap
            [array[i], array[i + 1]] = [array[i + 1], array[i]]
            // since we swap, recurssion
            bubbleSort(array)
        }
    }
    return array
}

// Test Cases
console.log(bubbleSort([])) // []
console.log(bubbleSort([1])) // [1]
console.log(bubbleSort([3, 1, 2, 4])) // [1, 2, 3, 4]
console.log(bubbleSort([-10, 1, 3, 8, -13, 32, 9, 5])) // [-13, -10, 1, 3, 5, 8, 9, 32]
