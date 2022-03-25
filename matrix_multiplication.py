import numpy as np 
import time

ntype = np.int64

class matriceMultplication:

  # def __init__(self, matrice_a_arr, matrice_b_arr) -> None:
  #     self.matrice_a_arr = matrice_a_arr
  #     self.matrice_b_arr = matrice_b_arr 


   def matrice_multiply_old_methode(self, matrice_a_arr, matrice_b_arr):
        n = matrice_a_arr.shape[0]
        matrice_c_arr = np.zeros((n, n))
        matrice_c_arr = matrice_c_arr.astype(ntype)
        for i in range(n):
            for j in range(n):
                matrice_c_arr[i, j] = 0
                for k in range(n):
                    matrice_c_arr[i, j] += matrice_a_arr[i, k] * matrice_b_arr[k, j]
        return matrice_c_arr
  
  
   def matrice_multiply_recursive_diviser_regner(self, matrice_a_arr, matrice_b_arr):
        n = matrice_a_arr.shape[0]
        matrice_c_arr = np.zeros((n, n))
        matrice_c_arr = matrice_c_arr.astype(ntype)
        if n == 1:
            matrice_c_arr[0, 0] = matrice_a_arr[0, 0] * matrice_b_arr[0, 0]
        else:
            demi_n = int(n / 2)
            matrice_c_arr[0 : demi_n, 0 : demi_n] = self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[0 : demi_n, 0 : demi_n], matrice_b_arr[0 : demi_n, 0 : demi_n]) + self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[0 : demi_n, demi_n : n], matrice_b_arr[demi_n : n, 0 : demi_n])
            matrice_c_arr[0 : demi_n, demi_n : n] = self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[0 : demi_n, 0 : demi_n], matrice_b_arr[0 : demi_n, demi_n : n]) + self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[0 : demi_n, demi_n : n], matrice_b_arr[demi_n : n, demi_n : n])
            matrice_c_arr[demi_n : n, 0 : demi_n] = self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[demi_n : n, 0 : demi_n], matrice_b_arr[0 : demi_n, 0 : demi_n]) + self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[demi_n : n, demi_n : n], matrice_b_arr[demi_n : n, 0 : demi_n])
            matrice_c_arr[demi_n : n, demi_n : n] = self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[demi_n : n, 0 : demi_n], matrice_b_arr[0 : demi_n, demi_n : n]) + self.matrice_multiply_recursive_diviser_regner(matrice_a_arr[demi_n : n, demi_n : n], matrice_b_arr[demi_n : n, demi_n : n])
        return matrice_c_arr

def main():
  matrice_a = np.random.randint(5, size=(16, 16))
  matrice_b = np.random.randint(5, size=(16, 16))
  matrice_multiplication = matriceMultplication()
  start = time.time()
  matrice_c_diviser = matrice_multiplication.matrice_multiply_recursive_diviser_regner(matrice_a, matrice_b)
  end = time.time()

  diviser_regner_time = end - start 

  start = time.time()
  matrice_c_old = matrice_multiplication.matrice_multiply_old_methode(matrice_a, matrice_b)
  end = time.time()

  old_methode_time = end - start 

  print(matrice_c_old)
  print(f"Temps écouler old methode {round(old_methode_time, 4)}\n\n")
  print(matrice_c_diviser)
  print(f'Temps écouler diviser regner {round(diviser_regner_time, 4)}')



if __name__ == '__main__':
  main()
