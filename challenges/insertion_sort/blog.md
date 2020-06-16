## Insertion Sort

<!-- Used a common sense guide to data structures and algorithms as source for conent on this page -->

### Pass 1
[Insertion_Sort_Pass1](../../assets/insertion_sort/insertion_sort_pass1.jpg)

- remove the value at index 1 and store it in a temporary variable


### Pass 2
[Insertion_Sort_Pass2](../../assets/insertion_sort/insertion_sort_pass2.jpg)

- compare the value of the temporary variable to the value 1 index less than where the temporary variable index. If the value to the left is greater than the temporary variable, then the left variable is now increased it's index by 1.


### Pass 3
[Insertion_Sort_Pass3](../../assets/insertion_sort/insertion_sort_pass3.jpg)

- The temp value will be inserted into the index that is empty

### Pass 4
[Insertion_Sort_Pass4](../../assets/insertion_sort/insertion_sort_pass4.jpg)

- remove the value at index 2 and store it in a temporary variable

### Pass 5
[Insertion_Sort_Pass5](../../assets/insertion_sort/insertion_sort_pass5.jpg)

- compare the value of the temporary variable to the value 2 index less than where the temporary variable index. If the value to the left is greater than the temporary variable, then the left variable is now increased it's index by 1. Repeat until there are no more values or the left variable is less than the temporary value.

### Pass 6
[Insertion_Sort_Pass6](../../assets/insertion_sort/insertion_sort_pass6.jpg)

- The temp value will be inserted into the index that is empty, index 0

### Pass 7
[Insertion_Sort_Pass7](../../assets/insertion_sort/insertion_sort_pass7.jpg)

- remove the value at index 3 and store it in a temporary variable

### Pass 8
[Insertion_Sort_Pass8](../../assets/insertion_sort/insertion_sort_pass8.jpg)

- compare the value of the temporary variable to the value 3 index less than where the temporary variable index. If the value to the left is greater than the temporary variable, then the left variable is now increased it's index by 1. Repeat until there are no more values or the left variable is less than the temporary value.

### Pass 9
[Insertion_Sort_Pass9](../../assets/insertion_sort/insertion_sort_pass9.jpg)

- The temp value will be inserted into the index that is empty, index 1


## Efficiency
- Time:0(n^2) given the nested while loop while require two loops, one for the length of the array and one for each interal loop which compares the current index to x number of indexes to the left within the array
- Space:0(n) given the array length is unknown
