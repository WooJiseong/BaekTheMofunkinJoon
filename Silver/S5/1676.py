"""
팩토리얼 0의 개수

문제
    N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
출력
    첫째 줄에 구한 0의 개수를 출력한다.

접근 방식 :
    뒤에서부터 0이 아닌 수가 나올 때 까지 0의 개수를 구한다는 뜻은, 해당 값에 10의 배수가 얼마나 포함되는지와 동치일 것이다.
    N부터 1까지 값을 줄여가며, 해당 값이 5로 나누어 떨어지면, 5에 해당하는 값을 +=1, 2로 나누어 떨어지면, 2에 해당하는 값에 +=1 하여, 두 값 중 Min 값을 출력하게 된다면, 해당 값이 나오게 될 것이다.
"""
N = int(input())
numOfTwo, numOfFive = 0,0

for temp in range(1,N+1):
    while temp % 5 == 0:
        temp/=5
        numOfFive+=1
    while temp % 2 == 0:
        temp/=2
        numOfTwo+=1
print(numOfFive if numOfFive<=numOfTwo else numOfTwo)

#추가적인 아이디어, 사실 수학적인 빈도 부분에서, 5의 배수가 2의 배수보다 많아질 수는 없지 않겠는가?
"""
N = int(input())
numOfFive = 0

for temp in range(1,N+1):
    while temp % 5 == 0:
        temp/=5
        numOfFive+=1
print(numOfFive)
"""

#추가적 아이디어, 모든 수를 검사할 필요가 있을까? 

"""
N = int(input())
count = 0
i = 5
while i <= N:
    count += N//i
    i *= 5
print(count)
"""