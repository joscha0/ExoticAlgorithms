import random

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def bogoSort(data):
    while not is_sorted(data):
        random.shuffle(data)
    return data

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Bogosort Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(bogoSort(list1)))