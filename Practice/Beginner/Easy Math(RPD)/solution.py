import itertools as it
testcases = int(input())
for _ in range(testcases):
    n = int(input())
    num_seq = list(map(int, input().split()))
    print(max(list(map(lambda x: sum(list(map(int, list(str(x[0]*x[-1]))))), it.combinations(num_seq, 2)))))
