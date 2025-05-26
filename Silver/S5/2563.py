N = int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int,input().split())
    for i in range(x, x+10):
        paper[i][y:y+10] = [1]*10

print(sum([sum(i) for i in paper]))