def solution(numbers):
    answer = 0
    answer_1 = 0
    for number in numbers:
        if answer <= number:
            answer = number
    numbers.remove(answer)
    for number in numbers:
        if answer_1 <= number:
            answer_1 = number
    return answer * answer_1