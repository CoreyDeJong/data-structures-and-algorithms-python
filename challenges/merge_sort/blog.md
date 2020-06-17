## Merge Sort

<!-- Used a common sense guide to data structures and algorithms as source for conent on this page -->

### Pass 1
[Merge_Sort_Pass1](../../assets/merge_sort/merge_sort_pass1.PNG)

- The array is divided into half​


### Pass 2
[Merge_Sort_Pass2](../../assets/merge_sort/merge_sort_pass2.PNG)

- The arrays are divided into half again​


### Pass 3
[Merge_Sort_Pass3](../../assets/merge_sort/merge_sort_pass3.PNG)

- The arrays are divided into half again​

### Pass 4
[Merge_Sort_Pass4](../../assets/merge_sort/merge_sort_pass4.PNG)

- The left value is compared to the value to the right, the smallest integer goes into the left position.

### Pass 5
[Merge_Sort_Pass5](../../assets/merge_sort/merge_sort_pass5.PNG)

- The left and right values are compared and sorted from smallest to largest

### Pass 6
[Merge_Sort_Pass6](../../assets/merge_sort/merge_sort_pass6.PNG)

- The left and right values are compared and sorted from smallest to largest



## Efficiency
- Time:0(n^2) given the nested while loop while require two loops, one for the length of the array and one for each interal loop which compares the current index to x number of indexes to the left within the array
- Space:0(n) given the array length is unknown
