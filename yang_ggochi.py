def solution(n, k):
    k = (k - (n // 10)) * 2000
    n = n * 12000
    answer = n + k
    return answer