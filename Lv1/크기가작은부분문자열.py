def solution(t, p):
    answer = 0
    result_list = []
    p_length = len(p)
    if(1<=p_length<=18):
        for i in range(len(t)):
            if(len(t[0+i:p_length+i]) == p_length):
                result_list.append(int(t[0+i:p_length+i]))
            else:
                print('길이가 {0}이 되지 않습니다'.format(p_length))
    
    print(result_list)
    for j in result_list:
        if(j <= int(p)):
            answer += 1
        else:
            print('{0}이 {1}보다 더 큽니다.'.format(j, p))
            
    return answer

print(solution('3141592', '271'))
print(solution('500220839878', '7'))
print(solution('10203', '15'))