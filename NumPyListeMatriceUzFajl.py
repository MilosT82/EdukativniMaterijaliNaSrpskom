#Formiranje liste u Pythonu
listaElemenata = ['a','b','c',['e','m'],'d','f',5,6,10,11.5]
print(listaElemenata)


#Pristupanje elementima liste pomocu indeksa
listaElemenata[3][1]

#Dodvanje Elementa na kraju liste
listaElemenata.append('DodatiElement')
print(listaElemenata)


#Kreiranje listi pomocu Numpy biblioteke
import numpy as np
L1 = np.array([1, 1])# jednodimenzionalna lista
print(L1)

L2 = np.array([[3, 2, 1], [7, 8, 9]]) # Dvodimenzionalna lista sa integerima
print(L2)

L3 = np.array([[3.5, 2, 1.0], [7.5, 8, 9.1]]) # Dvodimenzionalna lista sa realnim brojevima
print(L3)

L4 = np.array([3+7j, 2+8j, 1+9j], dtype = complex) # Jednodimenzionalna lista sa kompleksnim brojevima
print(L4)


#Drugi način kreiranja listi
L5 = np.arange(1,6) # kreiranje jednodimenzionalne liste integera od 1 do 5
#Ovde lista mora da ide do 6, jer indeksi u Python idu do nekog broja, ali ne obuhvataju i sam broj
print(L5)

L6 = np.ones(5) #kreiranje liste gde su svi elementi jedinice
print(L6)

L7 = np.zeros(5) #kreiranje liste gde su svi elementi nule
print(L7)

L8 = np.linspace(0,5,6) # Kreiranje liste brojeva sa jednakim intervalima
print(L8)

L9 = np.random.randn(5) # kreiranje liste brojeva sa normalnom raspodelom
print(L9)

L10 = np.random.randint(1,10,5) # kreiranje liste brojeva sa slučajnim brojevima
print(L10)


#Kreiranje matrica pomocu Numpy biblioteke
import numpy as np
M1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Kreiranje matrice koriscenjem naredbe array
print(M1)

M2 = np.arange(1,10).reshape(3,3) # Kreiranje matrice korscenjem naredbe reshape
print(M2)

M3 = np.array([L1,L1]) #Kreiranje matrice, spajanjem dve iste NumPy liste
print(M3)


P1 = [1, 2.5, 3]
P2 = [4, 5, 6]
M4 = np.array([P1,P2]) #Kreiranje matrice, spajanjem dve različite Python liste
print(M4)


M5 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Kreiranje matrice koriscenjem naredbe matrix
print(M5)


#Formiramo novu listu,ne matricu, pomocu dve liste L1
import numpy as np
L1 = np.array([1,1])# Dobija se dupla ista lista u okviru liste
DuplaLista=[L1,L1]
print(DuplaLista)

#Ako prvom elementu, promenimo vrednost na nulu, promenice se u obe liste
DuplaLista[0][0]=0
print(DuplaLista)

#Neka je data matrica sastavljena od dve spojene liste
#Ako se zada ista promena vrednosti na nulu, tada se samo prvi elemenat matrice manja na nulu
M3[0][0]=0
print(M3)

#Sabiranje matrica
import numpy as np
A = np.array([[1, 3, 1], [1, 5, 4], [1, 2, 4]])
B = np.array([[1, 2, 1], [-1, 4, 8], [-2, -1, 4]])
C = A + B      # pri sabiranju matrica se koristi plus
print(C)

# Mnozenje matrice skalarom
D = 2*A
print(D)

#Množenje matrica
import numpy as np
A = np.array([[1, 3, 1], [1, 5, 4], [1, 2, 4]])
B = np.array([[1, 2], [-1, 4], [-2, -1]])
C = A.dot(B) # mnozenje matrica sa naredbom dot 
print(C)

#Kod generisan od strane ChaGpt
import numpy as np

# Define the coefficient matrix and the constant matrix
A = np.array([[1, 2, 2],
              [1, -2, -3],
              [1, -1, -2]])
b = np.array([2, 0, 1])

# Find the inverse of A
A_inv = np.linalg.inv(A)

# Find the solution vector
x = np.dot(A_inv, b)

# Print the solution vector
print(f"x = {x[0]}")
print(f"y = {x[1]}")
print(f"z = {x[2]}")
