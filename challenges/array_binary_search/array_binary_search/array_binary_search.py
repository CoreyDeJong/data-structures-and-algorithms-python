def BinarySearch(array,n):
    arrayLength = len(array)
    lower_index = 0
    upper_index = len(array)-1
    middle = arrayLength//2

    while n != middle:
            if n == middle:
                return middle
    if middle < n:
            lower_index = middle +1           
    elif middle > n:
            upper_index = middle -1


# if __name__ == "__main__":
#     pass