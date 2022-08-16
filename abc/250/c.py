N = int(input())
winner = None
max_score = 0
words = set()
for i in range(N):
    S, T = input().split()
    T = int(T)
    if not S in words:
        words.add(S)
        if max_score < T:
            max_score = T
            winner = i
print(winner+1)