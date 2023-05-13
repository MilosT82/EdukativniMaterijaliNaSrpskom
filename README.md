# Numpy liste i matrice

### Autor: dr Milos Todorov
NAPOMENA: Materijal sa ovog repozitorijuma, pripremljen je i u vidu PDF, kao i propratni Python kod 
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

- **Liste u Pythonu mogu da sadrže stringove, brojeve, ili druge liste. One služe za skladištenje drugih objekata**

- **Elementima liste pristupamo pomoću indeksa, sa tim da u Pythonu indeksi kreću od nule**

- **Liste u Pythonu mogu da se proširuju, skraćuju, spajaju, kao i da se obriše deo liste. Python podržava mogućnost da se liste kreiraju u okviru liste**

- **Python ima sledeće tipove podataka koji mogu da se nađu u listama**

**Tabela 1:** Tipovi podataka u Pythonu
| Tip promenljive  | Objasnjenje |
| ------------- | ------------- |
|$${\color{red}String}$$ | Predstavljaju tekstualne podatke koji se prikazuju pod navodnicima, na primer ‘Lista’  |
|$${\color{red}Integer}$$ | Predstavljaju cele brojeve, na primer -2, 0, 5 |
|$${\color{red}Float}$$ | Predstavljaju realne brojeve, na primer 4.2, -3.6 |
|$${\color{red}Complex}$$ | Predstavljaju kompleksne brojeve, npr 3.0 + 2.0j  |
|$${\color{red}Boolean}$$ | Predstavlja tip koji može imati logičke vrednosti, tačno, ili netačno, odnosno True, ili False  |



### Formiranje liste u Pythonu

**Primer 1:** Formiranje liste u Pythonu
```python
listaElemenata = ['a','b','c',['e','m'],'d','f',5,6,10,11.5]
print(listaElemenata)
```

### Pristupanje elementima liste pomocu indeksa

**Primer 2:** Pristupanje elementu liste
```python
listaElemenata[3][1]
```




    'm'


Ovo je primer ugnježdene liste. Pošto indeksi u Pythonu kreću od nule, lista u okviru liste sa elementima ['e','m'] se nalazi na trećem indeksu, a elemenat 'm' je u okviru date liste na prvom mestu, tj.indeksu.

### Dodavanje Elementa na kraju liste

**Primer 3:** Dodavanje elementa na kraj listi
```python
listaElemenata.append('DodatiElement')
print(listaElemenata)
```

    ['a', 'b', 'c', ['e', 'm'], 'd', 'f', 5, 6, 10, 11.5, 'DodatiElement']
    
U prethodnom primeru 3. je prikazana jedna od metoda koja može da se primeni na Python listama. Sledi tabela sa metodama koje se koriste u okviru Python listi.

**Tabela 2:** Metode u okviru lista u Pythonu 
| Metoda  | Objasnjenje |
| ------------- | ------------- |
|$${\color{red}append()}$$ | Dodavanje elementa na kraju liste  |
|$${\color{red}clear()}$$ | Briše sve elemente liste |
|$${\color{red}copy()}$$ | Vraća kopiju liste |
|$${\color{red}count()}$$ | Prebraja elemente liste  |
|$${\color{red}extend()}$$ | Dodaje elemente neke druge liste, na kraj postojeće liste  |
|$${\color{red}index()}$$ | Vraća elemenat na definisanoj poziciji indeksa  |
|$${\color{red}insert()}$$ | Ubacuje elemenat u listu na određenu poziciju |
|$${\color{red}pop()}$$ | Briše elemenat u listi na određenoj poziciji indeksa |
|$${\color{red}remove()}$$ | Briše tačno određeni elemenat u listi koji se navede u okviru ove metode, odnosno naredbe   |
|$${\color{red}reverse()}$$ | Obrće elemente u listi  |
|$${\color{red}sort()}$$ | Sortira elemente u listi |

U prethodnoj tabeli 2. Prikazane su neke od naredbi koje mogu da se primene na Python listama. Pored python naredbi, postoji biblioteka NumPy, koja je pogodna za rad sa listama i matricama. Kreirao ju je Travis Oliphant 2005. godine.

Ova Python biblioteka se nalazi na sledećoj web adresi: 
<a href="https://numpy.org/">Numpy</a> 

Sledi prikaz date biblioteke.

## Prednosti biblioteke NumPy

Neke od prednosti korišćenja biblioteke Numpy:
- **NumPy kreira niz objekata koji je 50x puta brži od klasičnih Python listi** 

- **Niz objekata u NumPy se naziva ndarray, koji obezbeđuje korišćenje gomile funkcija sa listama**

- **Sadrži funkcije koje mogu da se koriste u matematičkim oblastima linearne algebre, Furijeove transformacije, kao i matricama, kao i mnogih drugih matematičkih funkcija**

- **Ima veliku upotrebu u oblasti veštačke inteligencije, odnosno pri korišćenju ML agoritama**

- **NumPy liste se smeštaju na jednom mestu u memoriji i iz tog razloga, lako im je pristupiti, što mogućava optimizaciju i brži rad sa listama**

- **Numpy ima mogućnost kreiranja različitih distribucija, kao što su Normalna, Poasonova, Uniformna, Logistička itd…**

- **Pored svega navedenog NumPy ima sve metode, kao i klasične Python liste, dok je lista tipova podataka proširena**


## Kreiranje listi pomocu Numpy biblioteke

- **Kod  Numpy listi važe sve operacije sa listama kao i kod klasičnih Python listi**

- **Elementima NumPy liste pristupamo takođe pomoću indeksa, kao što je prikazano u primeru 2**

Slede primeri kreiranja listi. Da bi se koristila neka biblioteka u Pythonu, ona mora da se pozove pomoću naredbe ${\color{red}import}$.

**Primer 4:** Kreiranje različitih Numpy listi


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

Postoji i drugi načini da kreiraju brojčane liste u zavisnosti od potrebe, a što će biti prikazano u narednom primeru.

**Primer 5:** Nekoliko drugih načina kreiranja Numpy listi


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
    
## Matrice

Neka je zadat sistem od $m$ linearnih jednačina sa $n$ nepoznatih $x_1,x_2, \cdots ,x_n$.

$$
\begin{matrix}
 a_{11} \cdot x_1+a_{12} \cdot x_2+ \cdots +a_{1 n} \cdot x_n=b_1 \\
 a_{21} \cdot x_1+a_{12} \cdot x_2+ \cdots +a_{2 n} \cdot x_n=b_2 \\
 \vdots \\
 a_{m 1} \cdot x_1+a_{m 2} \cdot x_2+ \cdots +a_{m n} \cdot x_n=b_m
\end{matrix}
$$

Brojevi $a_{ij}, b_i, i=1,2, \cdots ,m$, $j=1,2, \cdots ,n$ nazivaju se koeficijenti sistema.

**Matricom** nazivamo pravougaonu šemu oblika $m \times n$ sastavljenu od elemenata $a_{ij}$, raspoređenih u $m$ vrsta i $n$ kolona.

![image](https://github.com/MilosT82/NumpyListeMatrice/assets/84227323/6fec0704-fa20-4cee-b37c-bdfd51b6b378)

Matrica se može označiti na sledeći način $[a_{ij}]_{m \times n}$. Ova matrica ima koja ima $m$ vrsta i $n$ kolona ima dimenziju $m \times n$.
Matrica 

$$
\begin{bmatrix}
5 & 1 & 2\\
6 & 6 & 7
\end{bmatrix}
$$

je reda 2x3, jer ima 2 vrste i 3 kolone.

**NAPOMENA:** Determinanta je realan broj, koji je zapisan kao šema brojeva, za razliku od matrice koja je šema proizvoljnih elemenata.

Elementi  $a_{11}, a_{22},⋯,a_{mn}$  su na GLAVNOJ DIJAGONALI (označeno plavom bojom), a elementi $a_{1n},⋯,a_{m1}$  su na SPOREDNOJ DIJAGONALI (označeno crvenom bojom).

![image](https://github.com/MilosT82/NumpyListeMatrice/assets/84227323/6fdff449-85ef-4d6d-9134-6122a25b1980)

## Operacija sa matricama

### Sabiranje matrica

Zbir matrica $A =\left[a_{ij}  \right]$ i $B =\left[a_{ij}  \right]$ reda $m \times n$ je matrica $C = [c_{ij}]$,  $i=1,2, \cdots ,m$, $j=1,2, \cdots ,n$ koja je istog reda, gde je $\[a_{ij}\] + \[b_{ij}\] = \[c_{ij}\]$.

Mogu da se sabiraju samo matrice istih dimenzija. Sabira se svaki elemenat prve matrice sa odgovarajućim elementom druge matrice.

$$
C=A+B=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]+\left[\begin{array}{cccc}
b_{11} & b_{12} & \cdots & b_{1 n} \\
b_{21} & b_{22} & \cdots & b_{2 n} \\
\vdots & \vdots & & \vdots \\
b_{m 1} & b_{m 2} & \cdots & b_{m n}
\end{array}\right]=\left[\begin{array}{cccc}
c_{11} & c_{12} & \cdots & c_{1 n} \\
c_{21} & c_{22} & \cdots & c_{2 n} \\
\vdots & \vdots & & \vdots \\
c_{m 1} & c_{m 2} & \cdots & c_{m n}
\end{array}\right]
$$

Važe i sledeće osobine:
- Komutativnost $A+B=B+A$
- Asocijativnost $(A+B)+C=A+(B+C)$

**Primer 6:** Sabrati matrice:


$$
A= \begin{bmatrix}
1 & 3 & 1\\
1 & 5 & 4\\
1 & 2 & 4
\end{bmatrix} \text{i } 
B= \begin{bmatrix}
1 & 2 & 1\\
-1 & 4 & 8\\
-2 & -1 & 4
\end{bmatrix}
{.}$$

**Rešenje:**

$$
C=A+B= \begin{bmatrix}
1 & 3 & 1\\
1 & 5 & 4\\
1 & 2 & 4
\end{bmatrix} \text{+} 
\begin{bmatrix}
1 & 2 & 1\\
-1 & 4 & 8\\
-2 & -1 & 4
\end{bmatrix} \text{=}
\begin{bmatrix}
1+1 & 3+2 & 1+1\\
1-1 & 5+4 & 4+8\\
1-2 & 2-1 & 4+4
\end{bmatrix} \text{=}
\begin{bmatrix}
2 & 5 & 2\\
0 & 9 & 12\\
-1 & 1 & 8
\end{bmatrix}
$$

### Proizvod matrice sa skalarom

Proizvod matrice sa skalarom je matrica koja se dobije kada scalar $\gamma  \in  \mathbb{R}$ pomnožimo sa svakim elementom matrice $A =\left[a_{ij}  \right]$ reda $m \times n$.
$$\gamma \cdot A= A =\gamma \cdot \left[a_{ij}  \right]= \left[\gamma \cdot a_{ij}  \right]$$


$$
\gamma \cdot A=\gamma \cdot \left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]=\left[\begin{array}{cccc}
\gamma \cdot a_{11} & \gamma \cdot  a_{12} & \cdots & \gamma \cdot a_{1 n} \\
\gamma \cdot a_{21} & \gamma \cdot a_{22} & \cdots & \gamma \cdot  a_{2 n} \\
\vdots & \vdots & & \vdots \\
\gamma \cdot a_{m 1} & \gamma \cdot a_{m 2} & \cdots & \gamma \cdot a_{m n}
\end{array}\right]
$$

Važe i sledeće osobine:
- Komutativnost $\gamma \cdot A=A \cdot \gamma$
- Asocijativnost $(\alpha \cdot \beta) \cdot A=\alpha \cdot (\beta \cdot A)$
- Distributivnost u odnosu na zbir skalara $(\alpha+ \beta) \cdot A=\alpha \cdot A+\beta \cdot A$
- Distributivnost u odnosu na zbir matrica $\alpha \cdot (A+B)=\alpha \cdot A+\alpha \cdot B$

**Primer 7:** Pomnožiti matricu 

$$
A= \begin{bmatrix}
1 & 3 & 1\\
1 & 5 & 4\\
1 & 2 & 4
\end{bmatrix}$$ 

sa skalarom $\gamma = 2$.


**Rešenje:**

$$
2 \cdot A=2 \cdot \begin{bmatrix}
1 & 3 & 1\\
1 & 5 & 4\\
1 & 2 & 4
\end{bmatrix} \text{=}
\begin{bmatrix}
2 \cdot 1 & 2 \cdot 3 & 2 \cdot 1\\
2 \cdot 1 & 2 \cdot 5 & 2 \cdot 4\\
2 \cdot 1 & 2 \cdot 2 & 2 \cdot 4
\end{bmatrix} \text{=}
\begin{bmatrix}
2 & 6 & 2\\
2 & 10 & 8\\
2 & 4 & 8
\end{bmatrix}
$$


### Množenje matrica

Proizvod matrica je matrica $C =\left[c_{ij}  \right]$ reda $m \times n$ koja se dobije kada se pomnože matrica $A =\left[a_{ij}  \right]$ reda $m \times p$ matrica $B =\left[b_{ij}  \right]$ reda $p \times n$. Elementi matrice C se dobijaju na sledeći način:

$$ \sum_{k=1}^{p} {a_{ik} \cdot b_{kj}} \text{.}$$

Kada se prikaže pomoću koeficijenata imamo sledeći zapis.

$$
C=A \cdot B=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 p} \\
a_{21} & a_{22} & \cdots & a_{2 p} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m p}
\end{array}\right] \cdot \left[\begin{array}{cccc}
b_{11} & b_{12} & \cdots & b_{1 n} \\
b_{21} & b_{22} & \cdots & b_{2 n} \\
\vdots & \vdots & & \vdots \\
b_{p 1} & b_{p 2} & \cdots & b_{p n}
\end{array}\right]
$$

$$
C=\left[\begin{array}{cccc}
a_{11} \cdot b_{11}+a_{12} \cdot b_{21}+\cdots+a_{1 p} \cdot b_{p 1} & a_{11} \cdot b_{12}+a_{12} \cdot b_{22}+\cdots+a_{1 p} \cdot b_{p 2} & \cdots & a_{11} \cdot b_{1 n}+a_{12} \cdot b_{2 n}+\cdots+a_{1 p} \cdot b_{p n} \\
a_{21} \cdot b_{11}+a_{22} \cdot b_{21}+\cdots+a_{2 p} \cdot b_{p 1} & a_{21} \cdot b_{12}+a_{22} \cdot b_{22}+\cdots+a_{2 p} \cdot b_{p 2} & \cdots & a_{21} \cdot b_{1 n}+a_{22} \cdot b_{2 n}+\cdots+a_{2 p} \cdot b_{p n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} \cdot b_{11}+a_{m 2} \cdot b_{21}+\cdots+a_{m p} \cdot b_{p 1} & a_{m 1} \cdot b_{12}+a_{m 2} \cdot b_{22}+\cdots+a_{m p} \cdot b_{p 2} & \cdots & a_{m 1} \cdot b_{1 n}+a_{m 2} \cdot b_{2 n}+\cdots+a_{m p} \cdot b_{p n}
\end{array}\right]
$$

**Napomena:** Proizvod dve matrice je definisan samo ako je broj kolona prve matrice jednak sa brojem vrsta druge matrice!

Važe i sledeće osobina:
- Asocijativnost $(A \cdot B) \cdot C=A \cdot (B \cdot C)$

U opštem slučaju ne važi komutativnost $A \cdot B \neq B \cdot A$.

**Primer 8:** Pomnožiti matrice 

$$
A= \begin{bmatrix}
1 & 3 & 1\\
1 & 5 & 4\\
1 & 2 & 4
\end{bmatrix} \text{i } 
B= \begin{bmatrix}
1 & 2 \\
-1 & 4 \\
-2 & -1
\end{bmatrix}
{.}$$

**Rešenje:**

$$
C=A \cdot B= \begin{bmatrix}
1 & 3 & 1\\
1 & 5 & 4\\
1 & 2 & 4
\end{bmatrix} \cdot 
\begin{bmatrix}
1 & 2 \\
-1 & 4 \\
-2 & -1
\end{bmatrix} =
\begin{bmatrix}
1 \cdot 1+3 \cdot (-1)+1 \cdot (-2) & 1 \cdot 2+3 \cdot 4+1 \cdot (-1) \\
1 \cdot 1+5 \cdot (-1)+4 \cdot (-2) & 1 \cdot 2+5 \cdot 4+4 \cdot (-1) \\
1 \cdot 1+2 \cdot (-1)+4 \cdot (-2) & 1 \cdot 2+2 \cdot 4+4 \cdot (-1)
\end{bmatrix}
$$

$$
C=A \cdot B=
\begin{bmatrix}
1-3-2 & 2+12-1 \\
1-5-8 & 2+20-4 \\
1-2-8 & 2+8-4
\end{bmatrix} =
\begin{bmatrix}
-4 & 13 \\
-12 & 18 \\
-9 & 6
\end{bmatrix}
$$

### Transponovana matrica

Transponovana matrica je matrica u kojoj su vrste(kolone) zamenile mesta sa odgovarajućim kolonama(vrstama), odnosno za matricu $A=[a_{ij}]$ reda $m \times n$   njena transponovana matrica je $A^T=[a_{ji}]$ reda $n \times m$.



$$
A= \left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right] \Rightarrow
A^T= \left[\begin{array}{cccc}
a_{11} & a_{21} & \cdots & a_{m 1} \\
a_{12} & a_{22} & \cdots & a_{m 2} \\
\vdots & \vdots & & \vdots \\
a_{1 n} & a_{2 n} & \cdots & a_{m n}
\end{array}\right]
$$

**Primer 9:** Neka je data matrica

$$
A= \begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix} \text{.}
$$

Naći njenu transponovanu matricu.

**Resenje:**

$$
A= \begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix} \Rightarrow
A^T= \begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

## inverzna

$$
\begin{array}{llll}
A_{11} & =\left|\begin{array}{ll}
-2 & -3 \\
-1 & -2
\end{array}\right|=1 & A_{21}=-\left|\begin{array}{cc}
2 & 2 \\
-1 & -2
\end{array}\right|=2 & A_{31}=\left|\begin{array}{cc}
2 & 2 \\
-2 & -3
\end{array}\right|=-2 \\
A_{12} & =-\left|\begin{array}{ll}
1 & -3 \\
1 & -2
\end{array}\right|=-1 & A_{22}=\left|\begin{array}{cc}
1 & 2 \\
1 & -2
\end{array}\right|=-4 & A_{32}=-\left|\begin{array}{cc}
1 & 2 \\
1 & -3
\end{array}\right|=5 \\
A_{13} & =\left|\begin{array}{cc}
1 & -2 \\
1 & -1
\end{array}\right|=1 & A_{23}=-\left|\begin{array}{cc}
1 & 2 \\
1 & -1
\end{array}\right|=3 & A_{33}=\left|\begin{array}{cc}
1 & 2 \\
1 & -2
\end{array}\right|=-4
\end{array}
$$

## Kreiranje matrica pomocu Numpy biblioteke

Matrice dimenzija $m \times n$ mogu da se kreiraju pomoću biblioteke Numpy na više načina, a što će biti prikazano u narednim primerima. Najčešće se to radi uz pomoć naredbe array. Ovo je već prikazano kroz primer 2. kada su prikazane dvodimenzinalne liste L2 i L3, a sledi još jedan primer. Treba obratiti pažnju da se matrice definišu pomoću duplih uglastih zagrada, odnosno $[[ , ],[ , ], \cdots , [ , ]]$, a pri tom se mora voditi računa da su iste dužine liste, odnosno o dimenziji matrice. Slede primeri u kojima će biti prikazani načini kreiranja matrica.

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
    
