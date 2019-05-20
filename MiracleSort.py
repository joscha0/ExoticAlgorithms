import time

count = 0

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def miracleSort(lst):
    global count
    if(is_sorted(lst)):
        return lst
    else:
        if count <= 5:
            print('failed try again ' + str(5-count))
            count += 1
            miracleSort(lst)
        else:
            print('FAILED!')
            count = 0

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    list2 = [1,2,3,4,5,6,7]
    print('\n\n-----Miracle Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(miracleSort(list1)))