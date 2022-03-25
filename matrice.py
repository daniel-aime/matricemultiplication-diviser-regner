from operator import index
import random 

# Set random the matrix A and B
A = [ [random.randint(0, 10) for j in range(8)] for i in range(8) ]
B = [ [random.randint(0, 10) for j in range(8)] for i in range(8) ]

# a = [
#   [1, 2, 3],
#   [1, 4, 5],
#   [0, 2, 2]
# ]

# b = [
#   [1, 3, 4],
#   [0, 4, 4],
#   [2, 3, 1]
# ]

def parcourir(a, n):
  i = n
  if n == 0:
    print(a[0])
  else:
    i =  parcourir(a, i-1)
    print(a[i])
    
  return i +1 

"""
  On va fusionner les resultat obtenue de division de la problème
  
"""
def fusion():
  pass 



def produit_mat(vect_A, vect_B, n):
  somme = 0
  i = n
  
  if i == 0:
    somme += vect_A[0] * vect_B[0]
  else:
    tmp_somme  = 0
    somme += vect_A[i] * vect_B[i]
    tmp_somme , i = produit_mat(vect_A, vect_B, i-1)
    somme += tmp_somme  
  

  return (somme, i + 1)


# c = [1, 2] * [0, -1]

# print(produit_mat(a, b, len(a) - 1 ))

# a * b = 6
a = [
  [1, 2, 1],
  [4, 1, 2],
  [-7, 10, 2]
]
b = [
  [0, 1, 3],
  [-1, 2, 3],
  [4, 10, 3]
]
def slice_matrix(a, b, start, finish):
  a_pk = []
  b_kq = []

  for i in range(len(a)):
    a_pk.append(a[start][i])
    b_kq.append(b[i][finish])
  
  # print(f"La valeur du vec a_pk = {a_pk}")
  # print(f"La valeur du vect a_kq = {b_kq}")

  return (a_pk, b_kq)


def prod_mat_A_B(mat_A, mat_B, C=None, n_iteration=None):
  
  ligne = 0
  colonne = 0
  n = len(mat_A) - 1

  if C == None:
    C = [ [0 for j in range(len(mat_A))] for i in range(len(mat_A))]
    n_iteration = len(C) - 1


  if n_iteration == 0:
    a_pk, b_kp = slice_matrix(mat_A, mat_B, 0, 0)
    C[0][0] = produit_mat(a_pk, b_kp, n )[0]

  else: 
    a_pk, b_kp = slice_matrix(mat_A, mat_B, ligne, colonne)
    print(n_iteration)
    C[ligne][colonne] = produit_mat(a_pk, b_kp, n )[0]
    ligne, colonne, C, n_iteration = prod_mat_A_B(mat_A, mat_B, C, n_iteration - 1)
    print(ligne, colonne)


    
  
  return [ligne + 1, colonne + 1, C, n_iteration + 1]
  
print(prod_mat_A_B(A, B) )




# print(B)
# aa = 0
# while aa < len(a):
#   print(a[aa])
#   aa += 1





  

  





