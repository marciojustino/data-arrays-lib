import random
import numpy as np
from src.data_arrays import DataArrays
import datetime

a = np.random.randint(1, 10000, 1000000)

dataArrays = DataArrays()
start_at = datetime.datetime.now()
b = dataArrays.sort(a)
ends_at = datetime.datetime.now()
print("Duration: {}".format(ends_at-start_at))
