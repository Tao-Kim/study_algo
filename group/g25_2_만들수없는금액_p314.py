_ = int(input())

coins = list(map(int, input().split()))

possible_values = set()

for coin in coins:
    possible_values_copy = possible_values.copy()
    for possible_value in possible_values_copy:
        possible_values.add(possible_value + coin)

    possible_values.add(coin)
    
for num in range(1, 1000001):
    if num not in possible_values:
        print(num)
        break
    # try:
    #     possible_values.remove(num)
    # except:
    #     print(num)
    #     break