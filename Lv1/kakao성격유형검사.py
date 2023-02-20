def solution(survey, choices):
    answer = ''
    grade = {
        1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7:3
    }
    total_grade = {
        'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0
    }
    for i in range(len(survey)):
        if(choices[i] < 4):
            survey_english = list(survey[i])[0]
            total_grade[survey_english] += grade[choices[i]]
        elif(choices[i] > 4):
            survey_english = list(survey[i])[1]
            total_grade[survey_english] += grade[choices[i]]

    answer = result(total_grade)
    return answer

def result(total_grade):
    answer = ''

    if total_grade['R'] >= total_grade['T']:
        answer += 'R'
    elif total_grade['R'] < total_grade['T']:
        answer += 'T'

    if total_grade['C'] >= total_grade['F']:
        answer += 'C'
    elif total_grade['C'] < total_grade['F']:
        answer += 'F'

    if total_grade['J'] >= total_grade['M']:
        answer += 'J'
    elif total_grade['J'] < total_grade['M']:
        answer += 'M'

    if total_grade['A'] >= total_grade['N']:
        answer += 'A'
    elif total_grade['A'] < total_grade['N']:
        answer += 'N'
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))