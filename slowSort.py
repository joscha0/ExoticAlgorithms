def slowSort(A, i, j):
    if i >= j:
        return
    m = (i+j)//2
    slowSort(A, i, m)
    slowSort(A, m+1, j)
    if A[m] > A[j]:
        A[m],A[j] = A[j],A[m]
    slowSort(A, i, j-1)

if __name__ == "__main__":
    list1 = [1,4,2,5,6,5,3]
    print('\n\n-----Slowsort Sorting Algorithm-----\n')
    print('unsorted list:   '+str(list1))
    slowSort(list1, 0, len(list1)-1)
    print('sorted list:     '+str(list1))