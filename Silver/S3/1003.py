'''
피보나치 함수
'''
def count_fibonacci(N : int) -> int:
    countZero = 0
    countOne = 0
    if N == 0:
        return 1,0
    elif N == 1:
        return 0,1
    else:
        fibonacci = [1,1]
        while N >= 3:
            temp = fibonacci[0]+fibonacci[1]
            fibonacci[0] = fibonacci[1]
            fibonacci[1] = temp
            N-=1
        countZero = fibonacci[0]
        countOne = fibonacci[1]

    return countZero, countOne 

testCase = int(input())
for _ in range(testCase):
    N = int(input())
    print(*count_fibonacci(N))