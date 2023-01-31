def solution(s):
    answer = []
    word_dict = {}
    print()
    
    for idx, word in enumerate(list(s)):
        if word not in word_dict:
            answer.append(-1)
            word_dict[word] = idx
            print(word_dict)
        else:
            answer.append(idx - word_dict[word])
            word_dict[word] = idx
            print(word_dict)
            
    return answer

print(solution("banana"))
print(solution("foobar"))