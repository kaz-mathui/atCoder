n = int(input())
num_list = list(map(int,input().split()))
count_list = []
 
for x in num_list:
    count = 0
    while x%2 == 0:
        count += 1
        x /= 2
    count_list.append(count)
 
print(min(count_list))