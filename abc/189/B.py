from decimal import Decimal
N, X = map(int, input().split())
drink = 0
for i in range(1,N+1):
    drink_list = list(input().split())
    drink += Decimal(drink_list[0])*Decimal(drink_list[1])/Decimal('100')
    
    if drink > X:
        print(i)
        break
if drink <= X:
    print(-1)

# print(drink)