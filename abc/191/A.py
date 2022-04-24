# abc_list = list(map(int, list(input().split())))
# a, b = map(int, input().split())
V,T,S,D = map(int, input().split())

if V*T > D or V*S < D:
    print('Yes')
else:
    print('No')