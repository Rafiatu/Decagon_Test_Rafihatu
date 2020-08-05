def solution(A,K):
    if type(A) is list and type(K) is int:
        for x in A:
            return x in range(A[0],A[-K])

print(solution([1,2,3,4,5], 2))
