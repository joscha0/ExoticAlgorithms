from  BogoBogoSort import bogoBogoSort
from  BogoSort import bogoSort
from  BozoSort import bozoSort
from  CommunismSort import communismSort
from  MiracleSort import miracleSort
from  StalinSort import stalinSort
from  slowSort import slowSort
import numpy as np
import time

def time_it(func):
    start = time.time()
    func()
    end = time.time()
    print('sorted list: '+ str(func()))
    print('Finished in {} seconds.'.format(end - start))

algsList = [bogoBogoSort, bogoSort, bozoSort, communismSort, miracleSort, stalinSort, slowSort]

for alg in algsList:
    print('\n'+str(alg.__name__)+ '...')
    randlist = np.random.randint(0, 100, 5).tolist()
    print('unsorted list: ', randlist)
    time_it(lambda: alg(randlist))