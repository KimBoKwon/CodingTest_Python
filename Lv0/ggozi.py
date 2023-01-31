def solution(n, k):
    answer = 0
    ggozi = 12000
    drink = 2000
    print(n//10)
    if (n >= 10):
        answer = ggozi * n + drink * k - drink * (n//10)
    else:
        answer = ggozi * n + drink * k
    return answer

print(solution(10, 3))
print(solution(64, 6))