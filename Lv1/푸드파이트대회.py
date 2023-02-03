def solution(food):
    answer = ''
    resultArr = ['0']
    if(2 <= len(food) <= 9):
        for i in range(len(food), 1, -1):
            if food[i-1]%2 == 0:
                for j in range(food[i-1]//2):
                    resultArr.append('{0}'.format(i-1))
                for z in range(food[i-1]//2):
                    resultArr.insert(0, '{0}'.format(i-1))
            elif food[i-1]%2 != 0:
                for j in range((food[i-1]-1)//2):
                    resultArr.append('{0}'.format(i-1))
                for z in range((food[i-1]-1)//2):
                    resultArr.insert(0, '{0}'.format(i-1))
    
    print(resultArr)
    answer = "".join(resultArr)
    return answer

print(solution([1, 3, 4, 6]))
print(type(solution([1, 3, 4, 6])))