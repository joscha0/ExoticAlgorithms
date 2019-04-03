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

def bogoBogoSort(lst):
	index = 2
	while(not is_sorted(lst)):
		bogoSort(lst[:index])
		index += 1
		if(not is_sorted(lst[:index])):
			random.shuffle(lst)
			index = 2
	return lst

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Bogobogosort Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(bogoBogoSort(list1)))