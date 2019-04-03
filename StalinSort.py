def stalinSort(lst):
    sorted_list = [lst[0]]
    for i in lst[1:]:
        if i >= sorted_list[-1]:
            sorted_list.append(i)
    return sorted_list


if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Stalin Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(stalinSort(list1)))