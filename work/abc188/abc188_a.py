import numpy as np
X, Y = map(int, input().split())
diff = np.abs(X-Y)
if diff < 3:
    print('Yes')
else:
    print('No')
