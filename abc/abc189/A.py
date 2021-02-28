n = input()
n_list = list(str(n))
if n_list[0] == n_list[1] == n_list[2]:
    print('Won')
else:
    print('Lost')