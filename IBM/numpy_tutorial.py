import numpy as np
import math

### numpy --- multiple data values
# x=0
# print(np.sin(x))
##round , around an internal methord inside

in_array = [0, 1, 2, 3, 4]
in_array2 = [0, 1, 2, 3,4]
print(np.log(in_array))
print("\n cos values\n", np.cos(in_array))
print(np.sin(in_array))
print("round up=", np.reciprocal(np.sin(in_array)))

print(np.clip(in_array,a_min=3,a_max=7))