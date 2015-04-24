'''
Created on Apr 16, 2015

@author: rfsantacruz
'''
from pyCPPEngine import GPUAdder
import numpy as np
import numpy.testing as npt


arr = np.ones([2048], dtype=np.int32)
adder = GPUAdder(arr)
adder.increment()

adder.retreive_inplace()
results2 = adder.retreive()

npt.assert_array_equal(sum(arr), 4096)
npt.assert_array_equal(sum(results2), 4096)

print(results2)
print(arr) 

