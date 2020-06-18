## Quick Sort

### Pass 1
[Pass1](../../assets/quick_sort/quick_sort_pass1.PNG)

- Set the pivot to the right index of the array

### Pass 2
[Pass2](../../assets/quick_sort/quick_sort_pass2.PNG)

- Set the index that is left from the right index to the low and the index left of low to left –1. If left –1 is less than low, swap indexes​

### Pass 3
[Pass3](../../assets/quick_sort/quick_sort_pass3.PNG)

- Set the index of left –1 to low and the index left of left-1 to left –1. If left –1 is less than low, swap indexes

### Pass 4
[Pass4](../../assets/quick_sort/quick_sort_pass4.PNG)

- Set the index of left –1 to low and the index left of left-1 to left –1. If left –1 is less than low, swap indexes

### Pass 5
[Pass5](../../assets/quick_sort/quick_sort_pass5.PNG)

- Set the index of left –1 to low and the index left of left-1 to left –1. If left –1 is less than low, swap indexes

### Pass 6
[Pass6](../../assets/quick_sort/quick_sort_pass6.PNG)

- Swap the pivot value with the middle value​

### Pass 7
[Pass6](../../assets/quick_sort/quick_sort_pass7.PNG)

- Partition left of Middle: Set the index of left –1 to low and the index left of left-1 to left –1. If left –1 is less than low, swap indexes​

### Pass 8
[Pass6](../../assets/quick_sort/quick_sort_pass8.PNG)

- Partition Right of Middle: Set the index of middle +1 to low and the index right of right+1. If right+1 is less than low, swap indexes​

### Pass 9
[Pass6](../../assets/quick_sort/quick_sort_pass9.PNG)

- Partition Right : Set the index to the right of right+1 to right+1. If right+1 is less than low, swap indexes​

### Pass 10
[Pass6](../../assets/quick_sort/quick_sort_pass10.PNG)

- Partition Right : Increase the index of low to one index to the right and right+1 is set to one index right of low. If right+1 is less than low, swap indexes​
