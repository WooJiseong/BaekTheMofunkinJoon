longCable, shortCable = map(int, input().split())
cables = []
for _ in range(longCable):
    cables.append(int(input()))

length = 1
end = max(cables)

result = 0

while length <= end:
    mid = (length + end) // 2
    numCable = sum(cable // mid for cable in cables)

    if numCable >= shortCable:
        result, length = mid, mid + 1
    
    else:
        end = mid -1

print(result)