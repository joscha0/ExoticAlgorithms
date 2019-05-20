import random

def is_sorted(lst):
	cpy = lst[:]
	std = bogoBogoSort(cpy[:-1])
	while cpy[-1] < max(std):
		random.shuffle(cpy)
		std = bogoBogoSort(cpy[:-1])
	return std == lst[:-1]

def bogoBogoSort(lst):
	if len(lst) == 1:
		return lst
	while not is_sorted(lst):
		random.shuffle(lst)
	return lst

if __name__ == "__main__":
    list1 = [7,1,8,4,3]
    print('\n\n-----Bogobogosort Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(bogoBogoSort(list1)))