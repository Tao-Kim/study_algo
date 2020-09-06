n, c = map(int, input().split())

houses = sorted([int(input()) for _ in range(n)])

start = 1
end = houses[-1] - 1
result = -1

while start <= end:
    mid = (start + end ) // 2
    count = 1
    
    pre = houses[0]

    for i in range(1, n):
        if houses[i] >= pre + mid:
            count += 1
            pre = houses[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)