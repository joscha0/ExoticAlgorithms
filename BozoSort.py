import random

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def bozoSort(lst):
    while not is_sorted(lst):
        i, j = int(len(lst)*random.random()), int(len(lst)*random.random())
        lst[i], lst[j] = lst[j], lst[i]
    return lst
        
        
if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Bozosort Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(bozoSort(list1)))       