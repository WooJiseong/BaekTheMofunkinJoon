'''
어린왕자
'''
def judge_sep_circle(x1,y1,x2,y2):
    n = int(input())
    count = 0
    for i in range(n):
        circle = list(map(int,input().split()))
        circle_coor1_bool : bool = (circle[0]-x1)**2+(circle[1]-y1)**2 <= circle[2]**2
        circle_coor2_bool : bool = (circle[0]-x2)**2+(circle[1]-y2)**2 <= circle[2]**2
        if (circle_coor1_bool and not circle_coor2_bool) or (not circle_coor1_bool and circle_coor2_bool):
            count += 1
    return count

T = int(input())

for _ in range(T):
    coor = list(map(int,input().split()))
    print(judge_sep_circle(*coor))
