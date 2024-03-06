def solution(money):
    quotient = money // 5500
    remainder = money % 5500
    answer = [quotient, remainder]
    return answer