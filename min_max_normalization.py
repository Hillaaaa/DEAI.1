import numpy as np
def data_normalize(data):
    data = (data - np.min(data))/(np.max(data) - np.min(data))
    return data
data = np.array([5, 15, 25, 35, 45,55])
print(data_normalize(data))

