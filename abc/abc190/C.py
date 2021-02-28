N,M = map(int, input().split())
# print(dish_list)
ab_list = []
# 条件のデータを格納
for i in range(M):
    abi_list = []
    ai,bi = map(int, input().split())
    abi_list.append(ai-1)
    abi_list.append(bi-1)
    # Mこデータのリスト
    ab_list.append(abi_list)
K = int(input())
max_num = 0
cd_list = []
# K人が置く可能性のある場所を格納
for i in range(K):
    cdi_list = []
    ci,di = map(int, input().split())
    cdi_list.append(ci-1)
    cdi_list.append(di-1)
    cd_list.append(cdi_list)

for i in range(2**K):
    dish_list = [0] * N
    for j in range(K):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            dish_list[cd_list[j][0]] = 1
        else:
            dish_list[cd_list[j][1]] = 1
    
    count = 0
    for k in range(M):
        abi_list = ab_list[k]
        if dish_list[abi_list[0]] == 1 and dish_list[abi_list[1]] == 1:
            count += 1
            # print('dishList:',dish_list)
            # print('ab_list',ab_list)
            # print('cd_list',cd_list)
    max_num = max(max_num,count)
print(max_num)
