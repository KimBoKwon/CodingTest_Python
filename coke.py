def solution(a, b, n):
    answer = 0
    left_num = 0

    while n >= a:
        left_num = n%a
        n = (n//a) * b
        answer += n
        n += left_num

    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))