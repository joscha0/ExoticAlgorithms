def recSlowSort(A, i, j):
    if i >= j:
        return
    m = (i+j)//2
    recSlowSort(A, i, m)
    recSlowSort(A, m+1, j)
    if A[m] > A[j]:
        A[m],A[j] = A[j],A[m]
    recSlowSort(A, i, j-1)

def slowSort(lst):
    recSlowSort(lst, 0, len(lst)-1)
    return lst

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Slowsort Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    print('sorted list:     '+str(slowSort(list1)))