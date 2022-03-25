import numpy as np 
import time

ntype = np.int64

class MatrixMultplication:

  # def __init__(self, matrix_a_arr, matrix_b_arr) -> None:
  #     self.matrix_a_arr = matrix_a_arr
  #     self.matrix_b_arr = matrix_b_arr 


   def matrix_multiply_old_methode(self, matrix_a_arr, matrix_b_arr):
        n = matrix_a_arr.shape[0]
        matrix_c_arr = np.zeros((n, n))
        matrix_c_arr = matrix_c_arr.astype(ntype)
        for i in range(n):
            for j in range(n):
                matrix_c_arr[i, j] = 0
                for k in range(n):
                    matrix_c_arr[i, j] += matrix_a_arr[i, k] * matrix_b_arr[k, j]
        return matrix_c_arr
  
  
   def matrix_multiply_recursive_diviser_regner(self, matrix_a_arr, matrix_b_arr):
        n = matrix_a_arr.shape[0]
        matrix_c_arr = np.zeros((n, n))
        matrix_c_arr = matrix_c_arr.astype(ntype)
        if n == 1:
            matrix_c_arr[0, 0] = matrix_a_arr[0, 0] * matrix_b_arr[0, 0]
        else:
            half_n = int(n / 2)
            matrix_c_arr[0 : half_n, 0 : half_n] = self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[0 : half_n, 0 : half_n], matrix_b_arr[0 : half_n, 0 : half_n]) + self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[0 : half_n, half_n : n], matrix_b_arr[half_n : n, 0 : half_n])
            matrix_c_arr[0 : half_n, half_n : n] = self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[0 : half_n, 0 : half_n], matrix_b_arr[0 : half_n, half_n : n]) + self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[0 : half_n, half_n : n], matrix_b_arr[half_n : n, half_n : n])
            matrix_c_arr[half_n : n, 0 : half_n] = self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[half_n : n, 0 : half_n], matrix_b_arr[0 : half_n, 0 : half_n]) + self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[half_n : n, half_n : n], matrix_b_arr[half_n : n, 0 : half_n])
            matrix_c_arr[half_n : n, half_n : n] = self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[half_n : n, 0 : half_n], matrix_b_arr[0 : half_n, half_n : n]) + self.matrix_multiply_recursive_diviser_regner(matrix_a_arr[half_n : n, half_n : n], matrix_b_arr[half_n : n, half_n : n])
        return matrix_c_arr

def main():
  matrix_a = np.random.randint(5, size=(16, 16))
  matrix_b = np.random.randint(5, size=(16, 16))
  matrix_multipliaction = MatrixMultplication()
  start = time.time()
  matrix_c_diviser = matrix_multipliaction.matrix_multiply_recursive_diviser_regner(matrix_a, matrix_b)
  end = time.time()

  diviser_regner_time = end - start 

  start = time.time()
  matrix_c_old = matrix_multipliaction.matrix_multiply_old_methode(matrix_a, matrix_b)
  end = time.time()

  old_methode_time = end - start 

  print(matrix_c_old)
  print(f"Temps écouler old methode {round(old_methode_time, 4)}\n\n")
  print(matrix_c_diviser)
  print(f'Temps écouler diviser regner {round(diviser_regner_time, 4)}')



if __name__ == '__main__':
  main()
