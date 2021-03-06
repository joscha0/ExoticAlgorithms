import random

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def bogoSort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Bogosort Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(bogoSort(list1)))