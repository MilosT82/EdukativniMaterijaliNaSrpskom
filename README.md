# Numpy liste i matrice

### Autor: dr Milos Todorov

<div align="center">
 <h3>
	<img src="https://miro.medium.com/max/720/1*CDj-lEsfn9HAbpMSNmziLQ.gif"      width="300" 
     height="200"/>
</h3>
</div>


<h3 align="center">Milos Todorov PhD, univerzitetski profesor</h3>

- 🔭 Trenutno predajem na **fakultetu**

- 🌱 Trenutno izucavam **ML algortme**

- 📫 Mozete me kontaktirati na **milos.todorov82@gmail.com**


<h3 align="left">Linkedin konekcija:</h3>
<p align="left">
<a href="https://www.linkedin.com/in/milos-todorov-phd-2bb4a6201/" target="blank"><img align="center" img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/milos-todorov-phd-2bb4a6201/" height="30" width="40" /></a>
</p>

<h3 align="left">Programski jezik:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>



## Python Liste - kratki osvrt

### Formiranje liste u Pythonu


```python
listaElemenata = ['a','b','c',['e','m'],'d','f',5,6,10,11.5]
print(listaElemenata)
```

### Pristupanje elementima liste pomocu indeksa


```python
listaElemenata[3][1]
```




    'm'



### Dodavanje Elementa na kraju liste


```python
listaElemenata.append('DodatiElement')
print(listaElemenata)
```

    ['a', 'b', 'c', ['e', 'm'], 'd', 'f', 5, 6, 10, 11.5, 'DodatiElement']
    

## Kreiranje listi pomocu Numpy biblioteke


```python
import numpy as np
L1 = np.array([1, 1])# jednodimenzionalna lista
print('Lista L1: \n',L1)

L2 = np.array([[3, 2, 1], [7, 8, 9]]) # Dvodimenzionalna lista sa integerima
print('Lista L2: \n',L2)

L3 = np.array([[3.5, 2, 1.0], [7.5, 8, 9.1]]) # Dvodimenzionalna lista sa realnim brojevima
print('Lista L3: \n',L3)

L4 = np.array([3+7j, 2+8j, 1+9j], dtype = complex) # Jednodimenzionalna lista sa kompleksnim brojevima
print('Lista L4: \n',L4)
```

    Lista L1: 
     [1 1]
    Lista L2: 
     [[3 2 1]
     [7 8 9]]
    Lista L3: 
     [[3.5 2.  1. ]
     [7.5 8.  9.1]]
    Lista L4: 
     [3.+7.j 2.+8.j 1.+9.j]
    

### Drugi način kreiranja Numpy listi


```python

L5 = np.arange(1,6) # kreiranje jednodimenzionalne liste integera od 1 do 5
#Ovde lista mora da ide do 6, jer indeksi u Python idu do nekog broja, ali ne obuhvataju i sam broj
print('Lista L5: \n',L5)

L6 = np.ones(5) #kreiranje liste gde su svi elementi jedinice
print('Lista L6: \n',L6)

L7 = np.zeros(5) #kreiranje liste gde su svi elementi nule
print('Lista L7: \n',L7)

L8 = np.linspace(0,5,6) # Kreiranje liste brojeva sa jednakim intervalima
print('Lista L8: \n',L8)

L9 = np.random.randn(5) # kreiranje liste brojeva sa normalnom raspodelom
print('Lista L9: \n',L9)

L10 = np.random.randint(1,10,5) # kreiranje liste brojeva sa slučajnim brojevima
print('Lista L10: \n',L10)
```

    Lista L5: 
     [1 2 3 4 5]
    Lista L6: 
     [1. 1. 1. 1. 1.]
    Lista L7: 
     [0. 0. 0. 0. 0.]
    Lista L8: 
     [0. 1. 2. 3. 4. 5.]
    Lista L9: 
     [-1.42150501  1.24819973 -1.24384724 -1.03554861  0.3136415 ]
    Lista L10: 
     [9 4 2 7 5]
    

## Kreiranje matrica pomocu Numpy biblioteke


```python
import numpy as np
M1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Kreiranje matrice koriscenjem naredbe array
print('Matrica M1: \n',M1)

M2 = np.arange(1,10).reshape(3,3) # Kreiranje matrice korscenjem naredbe reshape
print('Matrica M2: \n',M2)

M3 = np.array([L1,L1]) #Kreiranje matrice, spajanjem dve iste NumPy liste
print('Matrica M3: \n',M3)


P1 = [1, 2.5, 3]
P2 = [4, 5, 6]
M4 = np.array([P1,P2]) #Kreiranje matrice, spajanjem dve različite Python liste
print('Matrica M4: \n',M4)


M5 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Kreiranje matrice koriscenjem naredbe matrix
print('Matrica M5: \n',M5)
```

    Matrica M1: 
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Matrica M2: 
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Matrica M3: 
     [[1 1]
     [1 1]]
    Matrica M4: 
     [[1.  2.5 3. ]
     [4.  5.  6. ]]
    Matrica M5: 
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    

### Formira se nova lista, ne matricu, pomocu dve liste L1


```python
import numpy as np
L1 = np.array([1,1])# Dobija se dupla ista lista u okviru liste
DuplaLista=[L1,L1]
print(DuplaLista)
```

    [array([1, 1]), array([1, 1])]
    

### Ako se prvom elementu promeni vrednost na nulu, promenice se u obe liste


```python
DuplaLista[0][0]=0
print(DuplaLista)
```

    [array([0, 1]), array([0, 1])]
    

### Neka je data matrica sastavljena od dve spojene liste. Ako se zada ista promena vrednosti na nulu, tada se samo prvi elemenat matrice manja na nulu


```python
M3[0][0]=0
print('Matrica M3 sa izmenjenim prvim elementom: \n',M3)
```

    Matrica M3 sa izmenjenim prvim elementom: 
     [[0 1]
     [1 1]]
    

### Sabiranje matrica


```python
import numpy as np
A = np.array([[1, 3, 1], [1, 5, 4], [1, 2, 4]])
B = np.array([[1, 2, 1], [-1, 4, 8], [-2, -1, 4]])
C = A + B      # pri sabiranju matrica se koristi plus
print('Zbir dve matrice je matrica C: \n',C)
```

    Zbir dve matrice je matrica C: 
     [[ 2  5  2]
     [ 0  9 12]
     [-1  1  8]]
    

### Mnozenje matrice skalarom


```python
D = 2*A
print('Matrica pomnozena skalarom je matrica D: \n',D)
```

    Matrica pomnozena skalarom je matrica D: 
     [[ 2  6  2]
     [ 2 10  8]
     [ 2  4  8]]
    

### Množenje matrica


```python
import numpy as np
A = np.array([[1, 3, 1], [1, 5, 4], [1, 2, 4]])
B = np.array([[1, 2], [-1, 4], [-2, -1]])
F = A.dot(B) # mnozenje matrica sa naredbom dot 
print('Proizvod dve matrice je matrica F: \n',F)
```

    Proizvod dve matrice je matrica F: 
     [[ -4  13]
     [-12  18]
     [ -9   6]]
    

## Kod generisan od strane ChaGpt za resavanje sistema linearnih jednacina matricnom metodom, koriscenjem biblioteke Numpy


```python
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
```

    x = 0.0
    y = 3.0
    z = -2.0
    
