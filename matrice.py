from operator import index
import random 

# Set random the matrix A and B
A = [ [random.randint(0, 10) for j in range(8)] for i in range(8) ]
B = [ [random.randint(0, 10) for j in range(8)] for i in range(8) ]

a = [
  [1, 2, 3],
  [1, 4, 5],
  [0, 2, 2]
]

b = [
  [1, 3, 4],
  [0, 4, 4],
  [2, 3, 1]
]

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

a = [
  [1, 2],
  [0, 1]
]
b = [
  [0, 1],
  [-1, 2]
]

# c = [1, 2] * [0, -1]

# print(produit_mat(a, b, len(a) - 1 ))

# a * b = 6

def slice_matrix(a, b, start, finish):
  

def prod_mat_A_B(mat_A, mat_B, C=None):
  
  ligne = 0
  colonne = 0
  if C == None:
    C = [ [0 for j in range(len(mat_A))] for i in range(len(mat_A))]
  else:
    
    if ligne == 0:
      n = len(mat_A) - 1
      C[0][0] = produit_mat(mat_A[0], mat_B[0], n )[0]
    else: 
      C[ligne][colonne] = 
    
  
  return [ligne + 1, colonne + 1]
  
  




# parcourir(B, len(B) - 1)
# print(B)
# aa = 0
# while aa < len(a):
#   print(a[aa])
#   aa += 1





  

  





