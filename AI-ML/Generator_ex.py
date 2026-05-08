number = 10000000000

"""
##WITHOUT GENERATORS
def get_numbers(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

nums = get_numbers(number)
"""

"""
##WITH GENERATORS
def numb_gen(n):
    for i in range(n):
        yield(i)

generated = numb_gen(number)
for i in range(number):
    print(next(generated))
"""

##ON GPU PROCESSING
import numpy as np
from numba_dpex import kernel, config
import dpctl

# 1. Define the GPU Kernel
@kernel
def fill_array_kernel(item_index, out_array):
    i = item_index[0]
    # This is your "calculation" running on the iGPU
    out_array[i] = i 

# 2. Setup the data (using a smaller size for the example)
results = np.zeros(number, dtype=np.int64)

# 3. Select the Intel iGPU
device = dpctl.select_default_device()
print(f"Running on: {device.name}")

# 4. Run on GPU
# We launch 'number' of threads to fill the array in parallel
fill_array_kernel[number](results)

# 5. Now you can print from the CPU
print(results)