from  BogoBogoSort import bogoBogoSort
from  BogoSort import bogoSort
from  BozoSort import bozoSort
from  CommunismSort import communismSort
from  MiracleSort import miracleSort
from  StalinSort import stalinSort
from  slowSort import slowSort
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pick import pick



def time_it(func):
    start = time.time()
    func()
    end = time.time()
    print('sorted list: '+ str(func()))
    print('Finished in {} seconds.'.format(end - start))
    return end - start

algsList = [bogoBogoSort, bogoSort, bozoSort, communismSort, miracleSort, stalinSort, slowSort]

title = 'Please choose a algorithm: '
options = ['bogoBogoSort', 'bogoSort', 'bozoSort', 'communismSort', 'miracleSort', 'stalinSort', 'slowSort']
option, index = pick(options, title)
alg_name = str(algsList[index].__name__)

times = []
max_n = int(input('Enter max n: '))

print('\n'+alg_name+ '...')
for i in range(1,max_n+1):
    randlist = np.random.randint(0, 100, i).tolist()
    print('\n'+'unsorted list: ', randlist)
    times.append(time_it(lambda: algsList[index](randlist)))

n = range(1,max_n+1)

fig, ax = plt.subplots()
ax.plot(n, times)

ax.set(xlabel='array length (n)', ylabel='time (s)',
       title=alg_name)
ax.grid()

fig.savefig("img/"+alg_name+".png")
plt.show()