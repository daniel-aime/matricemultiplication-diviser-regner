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
test = [1, 2, 3]

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


def produit_mat(mat_A, mat_B, ligne, col):
  pass

def prod_mat_A_B(mat_A, mat_B, C=None):
  
  ligne = 0
  colonne = 0
  if C == None:
    C = [ [0 for j in range(len(mat_A))] for i in range(len(mat_A))]
  else:
    
    if ligne == 0:
      C[1][1] = mat_A
    
  
  return [ligne + 1, colonne + 1]
  
  




parcourir(B, len(B) - 1)
print(B)
# aa = 0
# while aa < len(a):
#   print(a[aa])
#   aa += 1
  




  

  





