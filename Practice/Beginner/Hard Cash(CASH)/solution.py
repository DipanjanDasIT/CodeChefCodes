testcases = int(input())
for _ in range(testcases):
    main_details = list(map(int, input().split()))
    coin_details = list(map(lambda x: int(x)%main_details[-1], input().split()))
    print(sum(coin_details)%main_details[-1])
