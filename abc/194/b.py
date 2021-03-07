n = int(input())
persons = []
for i in range(n):
    a,b = map(int,input().split())
    persons.append([a,b,a+b])

min_time = 100000

for i in range(n):
    for j in range(n):
        if i == j:
            work_time = persons[i][0] + persons[j][1]
        else:
            work_time = max(persons[i][0],persons[j][1])
        min_time = min(min_time,work_time)
print(min_time)