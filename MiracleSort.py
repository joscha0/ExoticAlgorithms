import time

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def miracleSort(list):
    if(is_sorted(list)):
        return list
    else:
        time.sleep(1)
        miracleSort(list)

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    list2 = [1,2,3,4,5,6,7]
    print('\n\n-----Miracle Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(miracleSort(list1)))