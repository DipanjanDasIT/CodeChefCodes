testcases = int(input())
for _ in range(testcases):
    n = int(input())
    listA = sorted(list(map(int, input().split())))
    listB = sorted(list(map(int, input().split())))
    s = 0
    for i in range(n):
        s = s + min([listA[i], listB[i]])
    print(s)
