def BinarySearch(array, n):
        start =0
        end = len(array)-1

        while start <= end:
                middle = start + (end - start) //2
                mid_value = array[middle]

                if mid_value == n:
                        return middle
                
                elif n < mid_value:
                        end = middle -1
                
                else:
                        start = middle +1
        return -1

    

