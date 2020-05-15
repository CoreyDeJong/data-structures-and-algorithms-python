
##

def insertShiftArray(a,n):
    x = (len(a)//2)+1
    

    for i in range(0, len(a)+1):
        answer = []
        if i<x:
            answer.append(a[i])
        elif i ==x:
            answer.append(n)
        elif i >x:
            answer.append(a[i-1])
        i+=1

    return answer


if __name__ == "__main__":
    a = int(input())