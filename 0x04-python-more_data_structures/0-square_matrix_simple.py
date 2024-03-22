#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  M=[]
  for i in range(len(matrix)):
    L=[]
    for j in range(len(matrix)):
      r = matrix[i][j]*matrix[i][j]
      L.append(r)
    M.append(L)
  return M
