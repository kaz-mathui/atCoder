N = int(input())
data = []
for i in range(N):
    A, P, X = map(int, input().split())
    data.append([A, P, X])
# A:徒歩　P：金額　X：在庫
min_price = 10 ** 9

for i in range(N):
    A, P, X = data[i][0], data[i][1], data[i][2]
    left_good = X - A
    if left_good > 0:
        min_price = min(min_price, P)
if min_price == 10 ** 9:
    print(-1)
else:
    print(min_price)
