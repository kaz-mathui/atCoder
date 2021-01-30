A,B,C = map(int, input().split())
if C == 0:
    if A <= B:
        print('Aoki')
    else:
        print('Takahashi')
else:
    if A < B:
        print('Aoki')
    else:
        print('Takahashi')

