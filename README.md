# Numpy liste i matrice

**Autor:** dr Milos Todorov
**NAPOMENA:** Materijal sa ovog repozitorijuma, pripremljen je i u vidu PDF, kao i propratni Python kod 
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

## Sadrzaj

- [Python Liste - kratki osvrt](#python-liste---kratki-osvrt)
	- [Formiranje liste u Pythonu](#formiranje-liste-u-pythonu)
	- [Pristupanje elementima liste pomocu indeksa](#pristupanje-elementima-liste-pomocu-indeksa)
	- [Dodavanje elementa na kraju liste](#dodavanje-elementa-na-kraju-liste)
- [Prednosti biblioteke NumPy](#prednosti-biblioteke-numpy)
- [Kreiranje listi pomocu Numpy biblioteke](#kreiranje-listi-pomocu-numpy-biblioteke)
	- [Drugi način kreiranja Numpy listi](#drugi-način-kreiranja-numpy-listi)
- [Matrice](#matrice)
- [Operacija sa matricama](#operacija-sa-matricama)
	- [Sabiranje matrica](#sabiranje-matrica)
	- [Proizvod matrice sa skalarom](#proizvod-matrice-sa-skalarom)
	- [Množenje matrica](#množenje-matrica)
	- [Transponovana matrica](#transponovana-matrica)
- [Inverzna matrica](#inverzna-matrica)
- [Kreiranje matrica pomocu Numpy biblioteke](#kreiranje-matrica-pomocu-numpy-biblioteke)
- [Operacije sa matricama korišćenjem NumPy biblioteke](#operacije-sa-matricama-korišćenjem-numpy-biblioteke)
- [Kod generisan od strane ChaGpt za resavanje sistema linearnih jednacina matricnom metodom, koriscenjem biblioteke Numpy](#kod-generisan-od-strane-chagpt-za-resavanje-sistema-linearnih-jednacina-matricnom-metodom-koriscenjem-biblioteke-numpy)
- [Reference](#reference)

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

### Dodavanje elementa na kraju liste

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

![image](https://github.com/MilosT82/NumpyListeMatrice/assets/84227323/138dfe1a-6d5f-4ef1-8725-8ee73b73ce4b)

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

**Primer 10:** Neka je data matrica

$$
A= \begin{bmatrix}
1 & 4 & 7\\
2 & 5 & 8 \\
3 & 6 & 9
\end{bmatrix} \text{.}
$$

Naći njenu transponovanu matricu.

**Resenje:**

$$
A= \begin{bmatrix}
1 & 4 & 7\\
2 & 5 & 8 \\
3 & 6 & 9
\end{bmatrix} \Rightarrow
A^T= \begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

## Inverzna matrica

**Inverzna matrica** je kvadratna matrica $A^{-1}$, koja zadovoljava sledeću osobinu $A^{-1} \cdot A=A \cdot A^{-1}=I$, gde je $I$ jedinična matrica.

Kvadratna matrica A je **regularna** ako je $detA \neq 0$, dok je **singularna** ako je $detA=0$.
**Minor** $M_{ij}$ je determinanta koje sa dobija kada iz determinante D odbacimo $i$-tu vrstu i $j$-kolonu. 
Minor $M_{33}$ se nalazi na sledeći način.

![image](https://github.com/MilosT82/NumpyListeMatrice/assets/84227323/49409e03-394d-411d-99ec-118f0fc25dc4)

**Adjugovana matrica** matrice A u oznaci $adjA$ je transponovana kvadratna matrica koja se dobija od kofaktora matrice A.

$$
adjA= \left[\begin{array}{cccc}
A_{11} & A_{21} & \cdots & A_{m 1} \\
A_{12} & A_{22} & \cdots & A_{m 2} \\
\vdots & \vdots & & \vdots \\
A_{1 n} & A_{2 n} & \cdots & A_{m n}
\end{array}\right]
$$

Inverzna matrica $A^{-1}$ koja se dobija od kvadratne regularne matrice A jednaka je:
$A^{-1}= \frac{1}{detA} \cdot adjA$


**Primer 12:** Naći inverznu matricu $A^{-1}$ matrice

$$
A= \begin{bmatrix}
1 & 1 & 2\\
1 & 3 & 1 \\
4 & 1 & 1
\end{bmatrix} \text{.}
$$

**Rešenje:**

![image](https://github.com/MilosT82/NumpyListeMatrice/assets/84227323/18de16a0-cd82-4705-8a62-63d32f287f4d)


<!-- 
$$
\[
\text{{det}}(A) = \left| \begin{array}{{ccc}}
a & b & c \\
d & e & f \\
g & h & i \\
\end{array} \right| = (aei + bfg + cdh) - (ceg + bdi + afh)
\]
$$

$$
\begin{matrix}
A_{11}=(-1)^{1+1} \cdot \begin{bmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{bmatrix} =\begin{vmatrix}
3 & 1 \\
1 & 1
\end{vmatrix}=2 & 
A_{21}=(-1)^{2+1} \cdot\begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix}=-\begin{vmatrix}
1 & 2 \\
1 & 1
\end{vmatrix}=1 & 
A_{31}=(-1)^{3+1} \cdot\begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix}=\begin{vmatrix}
1 & 2 \\
3 & 1
\end{vmatrix}=-5\\
1 & 1 & 1 \\
2 & 2 & 2
\end{matrix}
$$


$$
\begin{aligned}
&A_{11}=(-1)^{1+1} \cdot \begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix} =\begin{vmatrix}
3 & 1 \\
1 & 1
\end{vmatrix}=2 A_{21}=(-1)^{2+1} \cdot\begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix}=-\begin{vmatrix}
1 & 2 \\
1 & 1
\end{vmatrix}=1 \quad A_{31}=(-1)^{3+1} \cdot\begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix}=\begin{vmatrix}
1 & 2 \\
3 & 1
\end{vmatrix}=-5\\
&A_{12}=(-1)^{1+2} \cdot\begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix}=-\begin{vmatrix}
1 & 1 \\
4 & 1
\end{vmatrix}=3 \quad A_{22}=(-1)^{2+2} \cdot\begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix}=\begin{vmatrix}
1 & 2 \\
4 & 1
\end{vmatrix}=-7 \quad A_{32}=(-1)^{3+2} \cdot\begin{vmatrix}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{vmatrix}=-\begin{vmatrix}
1 & 2 \\
1 & 1
\end{vmatrix}=1\\
&A_{13}=(-1)^{1+3} \cdot\left|\begin{array}{lll}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{array}\right|=\left|\begin{array}{ll}
1 & 3 \\
4 & 1
\end{array}\right|=-11 \quad A_{23}=(-1)^{2+3} \cdot\left|\begin{array}{lll}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{array}\right|=-\left|\begin{array}{ll}
1 & 1 \\
4 & 1
\end{array}\right|=3 \quad A_{33}=(-1)^{3+3} \cdot\left|\begin{array}{lll}
1 & 1 & 2 \\
1 & 3 & 1 \\
4 & 1 & 1
\end{array}\right|=\left|\begin{array}{ll}
1 & 1 \\
1 & 3
\end{array}\right|=2
\end{aligned}
$$


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
-->

## Kreiranje matrica pomocu Numpy biblioteke

Matrice dimenzija $m \times n$ mogu da se kreiraju pomoću biblioteke Numpy na više načina, a što će biti prikazano u narednim primerima. Najčešće se to radi uz pomoć naredbe array. Ovo je već prikazano kroz primer 2. kada su prikazane dvodimenzinalne liste L2 i L3, a sledi još jedan primer. Treba obratiti pažnju da se matrice definišu pomoću duplih uglastih zagrada, odnosno $[[ , ],[ , ], \cdots , [ , ]]$, a pri tom se mora voditi računa da su iste dužine liste, odnosno o dimenziji matrice. Slede primeri u kojima će biti prikazani načini kreiranja matrica.

**Primer 13:** Kreiranje matrice korišćenjem naredbe array




```python
import numpy as np
M1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Kreiranje matrice koriscenjem naredbe array
print('Matrica M1: \n',M1)
```

    Matrica M1: 
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
  
  
Takođe matrica može da se napravi od jednodimenzionalnog niza elemenata, pomoću naredbe ${\color{red}reshape}$ .
Kada se koristi ova naredba, mora se obratiti pažnja na dimenzije matrice.
U narednom primeru biće kreiran jednodimenzionalni niz brojeva od 1 do 9, ali uz pomoć naredbe numpy naredbe arange, koja je prikazana u primeru 5. Korišćenjem date naredbe dobiće se matrica dimenzije 3x3.



**Primer 14:** Kreiranje matrice korišćenjem naredbe reshape


```python
import numpy as np
M2 = np.arange(1,10).reshape(3,3) # Kreiranje matrice korscenjem naredbe reshape
print('Matrica M2: \n',M2)
```

    Matrica M2: 
     [[1 2 3]
     [4 5 6]
     [7 8 9]]

Matrica može da nastane više listi, ili jedne iste, ali moraju biti iste dužine, a što će biti prikazano u naredna dva primera, korišćenjem prethodno definisanih lista iz primera 4.

**Primer 15:** Kreiranje matrice spajanjem dve iste liste L1


```python
import numpy as np
M3 = np.array([L1,L1]) #Kreiranje matrice, spajanjem dve iste NumPy liste
print('Matrica M3: \n',M3)
```

    Matrica M3: 
     [[1 1]
     [1 1]]
    

**Primer 16:** Kreiranje matrice spajanjem dve različite Python liste


```python
import numpy as np
P1 = [1, 2.5, 3]
P2 = [4, 5, 6]
M4 = np.array([P1,P2]) #Kreiranje matrice, spajanjem dve različite Python liste
print('Matrica M4: \n',M4)
```

    Matrica M4: 
     [[1.  2.5 3. ]
     [4.  5.  6. ]]

Postoji mogućnost da se kreira matrica i pomoću naredbe  ${\color{red}matrix}$.

**Primer 17:** Kreiranje matrice korišćenjem naredbe matrix


```python
import numpy as np
M5 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Kreiranje matrice koriscenjem naredbe matrix
print('Matrica M5: \n',M5)
```

    Matrica M5: 
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    

Ako spojimo dve liste L1 iz primera 4. na sledeći način, dobićemo listu, koja liči na matricu, ali nije, nego je dupla ista lista.

**Primer 18:** Spajanje dve liste u jednu listu



```python
import numpy as np
L1 = np.array([1,1])# Dobija se dupla ista lista u okviru liste
DuplaLista=[L1,L1]
print(DuplaLista)
```

    [array([1, 1]), array([1, 1])]
    

Ako prvom elementu promenimo vrednost na nula, vrednost nula ćemo imati u obe liste, jer je ista lista, a što se vidi iz narednog primera.

**Primer 19:** Dodeliti prvom elementu liste vrednost nula



```python
DuplaLista[0][0]=0
print(DuplaLista)
```

    [array([0, 1]), array([0, 1])]
    

Ako istu dodelu vrednosti nula primenimo na matricu M3, iz primera 15. Koja se isto sastoji iz duple liste L1, dobija se vrednost nula na prvom elementu matrice, jer je to matrica, a ne lista. Upravo na ovaj primer treba obratiti pažnju. Sledi primer koji prikazuje promenu vrednosti matrice.

**Primer 20:** Promeniti vrednosti prvog elementa matrice na nulu



```python
M3[0][0]=0
print('Matrica M3 sa izmenjenim prvim elementom: \n',M3)
```

    Matrica M3 sa izmenjenim prvim elementom: 
     [[0 1]
     [1 1]]
    

## Operacije sa matricama korišćenjem NumPy biblioteke

Za prikaz ovih operacije biće korišćeni primeri koji su prethodno objašnjeni u okviru poglavlja Operacije sa matricama. Za početak sledi primer sabiranja matrica, korišćenjem matrica iz primera 6.

**Primer 21:** Sabrati matrica


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
    
Iz prethodnog primera može se uočiti da se rezultati podudaraju, sa primerom 6.
Sledi primer množenja matrice sa skalarom. Za ovo će biti koriščen primer 7. iz istog poglavlja. Kada se matrica množi sa skalarom, koristi se klasična operacija množenja($\cdot$).

**Primer 22:** Pomnožiti matricu skalarom



```python
D = 2*A
print('Matrica pomnozena skalarom je matrica D: \n',D)
```

    Matrica pomnozena skalarom je matrica D: 
     [[ 2  6  2]
     [ 2 10  8]
     [ 2  4  8]]
    

Kada se množe dve matrice, tada ne može da se koristi klasično množenje, nego se koristi Numpy funkcija dot. Sledi primer množenja matrica.

**Primer 23:** Pomnožiti dve matrice


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

U okviru ovog poglavlja biće prikazan Python kod za rešavanje sistema lineranih jednačina matričnom metodom, ali uz upotrebu NumPy bibliotke. Kod je izgenerisan primenom veštačke inteligencije **ChatGPT**. Biće prikazan kompletan matematički postupak rešavanja narednog primera, radi boljeg razumevanja zadatka. Dobijeni rezultati su **identični**.

**Primer 24:** Rešiti sistem jednačina matričnom metodom.

$$
\begin{matrix}
x+2y+2z=2 \\
x-2y-3z=0 \\
x-y-2z=1
\end{matrix}
$$

**Rešenje:**

![image](https://github.com/MilosT82/NumpyListeMatrice/assets/84227323/170c4709-de84-45d4-b980-04fd3f3f79c7)


U narednom primeru prikazan je kod koji je izgenerisao ChatGpt.

**Primer 25:** Prikazati Python kod izgenerisan od strane ChatGPTza resavanje sistema lin. jednačina

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
    

## Reference

1. https://www.programiz.com/python-programming/matrix
2. https://www.w3schools.com/python/numpy/numpy_intro.asp
3. https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array
4. https://numpy.org/doc/stable/reference/generated/numpy.matrix.html
5. https://www.digitalocean.com/community/tutorials/concatenate-lists-python
6. https://openai.com/product/gpt-4
