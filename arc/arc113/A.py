def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

K = int(input())
S_list = make_divisors(K)

count = 0
for h in range(1,K+1):
    for i in range(1,K+1):
        if i*h > K:
            break
        for j in range(1,K+1):
            if h*i* j > K:
                break
            if h*i* j <=K:
                count += 1
print(count)