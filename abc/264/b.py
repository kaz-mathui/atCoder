R, C = map(int, input().split())
 
#奇数行の時
if R % 2 == 1:
    #半分以下の時
    if R <= 7:
        odd = (R - 1) // 2
        if C % 2 == 0 and (C <= 2 * odd or C >= 15 - odd):
            print('white')
        else:
            print('black')
    #半分以上の時
    else:
        #行数を変換
        R_2 = 16 - R
        odd = (R_2 - 1) // 2
        if C % 2 == 0 and (C <= 2 * odd or C >= 15 - odd):
            print('white')
        else:
            print('black')
#偶数行の時
else:
    if R <= 8:
        if C % 2 == 1 and (C <= R - 1 or C >= 17 - R):
            print('black')
        else:
            print('white')
    else:
        #行数変換
        R_2 = 16 - R
        if C % 2 == 1 and (C <= R_2 - 1 or C >= 17 - R_2):
            print('black')
        else:
            print('white')