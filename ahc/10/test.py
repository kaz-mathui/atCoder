n = 30
t = [list([0,0,0]) for _ in range(n)]

# best = calc_score(t)
base_t = [ti[:] for ti in t]
print(base_t)
print(t)
print(t == base_t)
print(0^2)