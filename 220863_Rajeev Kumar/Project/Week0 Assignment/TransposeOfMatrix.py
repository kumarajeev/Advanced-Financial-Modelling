import pandas as pd 
import numpy as np
 
Matrix = np.array([[2, 1, 4, 8],
                    [1, 3,  4,2],
                    [3, 6, 1, 7],
                    [6, 0, 4, 6]],)

# finding the transpose of the given matrix
transposeofmatrix = Matrix.T

print(transposeofmatrix)

# reshaping of the transposed matrix
reshapedmatrix = transposeofmatrix.reshape(2,8)
print(reshapedmatrix)







