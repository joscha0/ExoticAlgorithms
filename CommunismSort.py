def communismSort(lst):
    avg = sum(lst) / len(lst) 
    for i in range(len(lst)):
        lst[i] = avg
    return lst

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Communism Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(communismSort(list1)))