
a = int(input())
# a = [1,2,3,4,5,-6]

def reverseArray():
    a_length = len(a)
    for i in range(1,a_length+1):
        print(a[a_length-i])
        i+=1

reverseArray()

