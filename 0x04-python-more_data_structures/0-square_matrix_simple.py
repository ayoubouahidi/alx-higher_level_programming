#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  M=[]
  for i in range(3):
    L=[]
    for j in range(3):
      r = matrix[i][j]*matrix[i][j]
      L.append(r)
    M.append(L)
  return M
