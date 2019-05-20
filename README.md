<h1 align="center">Exotic Algorithms</h1>
<p align="center">
  Exotic, stupid, funny algorithms
</p>
<p align="center">
  <a target="_blank" href="https://github.com/joscha0/ExoticAlgorithms" title="Source: GitHub"><img src="https://img.shields.io/badge/source-GitHub-303030.svg?style=flat-square"></a>
  <a target="_blank" href="https://choosealicense.com/licenses/mit/" title="License: MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square"></a>
  <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-3.6-blue.svg"/></a>
</p>
<p align="center">
  <a target="_blank" href="https://github.com/joscha0/ExoticAlgorithms"><img src="https://img.shields.io/github/watchers/joscha0/ExoticAlgorithms.svg?style=social&label=Watch" alt="github watchers">   </a>
  <a target="_blank" href="https://github.com/joscha0/ExoticAlgorithms"><img src="https://img.shields.io/github/stars/joscha0/ExoticAlgorithms.svg?style=social&label=Star" alt="github stars">   </a>
  <a target="_blank" href="https://github.com/joscha0/ExoticAlgorithms" title="Follow @joscha0 on GitHub"><img src="https://img.shields.io/github/followers/joscha0.svg?style=social&label=Follow" alt="GitHub followers">
  </a>
</p>

 - [BogoBogoSort](https://github.com/joscha0/ExoticAlgorithms/blob/master/BogoBogoSort.py "BogoBogoSort")
 - [BogoSort](https://github.com/joscha0/ExoticAlgorithms/blob/master/BogoSort.py "BogoSort")
 - [BozoSort](https://github.com/joscha0/ExoticAlgorithms/blob/master/BozoSort.py "BozoSort")
 - [CommunismSort](https://github.com/joscha0/ExoticAlgorithms/blob/master/CommunismSort.py "CommunismSort")
 - [MiracleSort](https://github.com/joscha0/ExoticAlgorithms/blob/master/MiracleSort.py "MiracleSort")
 - [StalinSort](https://github.com/joscha0/ExoticAlgorithms/blob/master/StalinSort.py "StalinSort")
 - [SlowSort](https://github.com/joscha0/ExoticAlgorithms/blob/master/SlowSort.py "SlowSort")

## Getting Started

Run each file or import them into your projects

### Prerequisites
* [python 3](https://www.python.org/downloads/) - the programming language used

To run run.py:
* **numpy**  [![Pypi](https://img.shields.io/pypi/v/numpy.svg?style=flat-square)](https://pypi.org/project/numpy/)
* **pick**  [![Pypi](https://img.shields.io/pypi/v/pick.svg?style=flat-square)](https://pypi.org/project/pick/)

To run runplot.py:
* **numpy**  [![Pypi](https://img.shields.io/pypi/v/numpy.svg?style=flat-square)](https://pypi.org/project/numpy/)
* **matplotlib**  [![Pypi](https://img.shields.io/pypi/v/matplotlib.svg?style=flat-square)](https://pypi.org/project/matplotlib/)
* **pick**  [![Pypi](https://img.shields.io/pypi/v/pick.svg?style=flat-square)](https://pypi.org/project/pick/)

Install all the required packages
```bash
pip3 install -r requirements.txt
```
You may also need to install tkinter
```bash
sudo apt-get install python3-tk
```

## Running the tests

Run the files with:
```
python3 file.py
```
or put the file in your project folder and import it
```
import file
```

## Algorithms
### BogoBogoSort
* **Best Case:** O(n)
* **Average Case:** O(n * (n!)n)
* **Worst Case:** ∞
```python
def bogoBogoSort(lst):
	index = 2
	while(not is_sorted(lst)):
		bogoSort(lst[:index])
		index += 1
		if(not is_sorted(lst[:index])):
			random.shuffle(lst)
			index = 2
	return lst
```
![](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/bogoBogoSort.png)

### BogoSort
* **Best Case:** O(n)
* **Average Case:** O(n!)
* **Worst Case:** ∞
```python
def bogoSort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst
```
![](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/bogoSort.png)

### BozoSort
* **Best Case:** O(n)
* **Average Case:** O(n!)
* **Worst Case:** ∞

```python
def bozoSort(lst):
    while not is_sorted(lst):
        i, j = int(len(lst)*random.random()), int(len(lst)*random.random())
        lst[i], lst[j] = lst[j], lst[i]
    return lst
```

![](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/bozoSort.png)

### CommunismSort
* **Best Case:** O(n)
* **Average Case:** O(n)
* **Worst Case:** O(n)

```python
def communismSort(lst):
    avg = sum(lst) / len(lst) 
    for i in range(len(lst)):
        lst[i] = avg
    return lst
```

![](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/communismSort.png)

### MiracleSort
* **Best Case:** O(n)
* **Average Case:** ∞
* **Worst Case:** ∞

```python
def miracleSort(lst):
    if(is_sorted(lst)):
        return lst
    else:
        miracleSort(lst)
```

![](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/miracleSort.png)

### StalinSort
* **Best Case:** O(n)
* **Average Case:** O(n)
* **Worst Case:** O(n)

```python
def stalinSort(lst):
    sorted_list = [lst[0]]
    for i in lst[1:]:
        if i >= sorted_list[-1]:
            sorted_list.append(i)
    return sorted_list
```

![](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/stalinSort.png)

### SlowSort
* **Best Case:** O(n ^ (lg n))
* **Average Case:** O(n ^ (lg n))
* **Worst Case:** O(n ^ (lg n))

```python
def slowSort(A, i, j):
    if i >= j:
        return
    m = (i+j)//2
    slowSort(A, i, m)
    slowSort(A, m+1, j)
    if A[m] > A[j]:
        A[m],A[j] = A[j],A[m]
    slowSort(A, i, j-1)
```

![](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/slowSort.png)
