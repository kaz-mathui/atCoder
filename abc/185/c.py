from scipy.special import comb
l = int(input())
base =comb(l-1, 11, exact=True)
print(base)