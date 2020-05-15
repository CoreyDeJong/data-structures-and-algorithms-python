
## test

def matrix_arr(arr):
    answer=[]
    for x in range(len(arr)):
        total=0
        for y in range(len(arr[x])):
            total += (arr[x][y])
        answer.append(total)
    return answer

if __name__ == "__main__":
    a = int(input())