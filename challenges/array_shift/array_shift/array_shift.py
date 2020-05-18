

def insertShiftArray(array, new_number):
    middle = (len(array)//2)-1
    
    
    answer = []

    for i in range(len(array)):
        answer.append(array[i])
        if i == middle:
            answer.append(new_number)
        i+=1

    return answer

