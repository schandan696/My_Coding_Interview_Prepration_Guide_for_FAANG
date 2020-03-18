'''
Algorithm for Selection sort
'''
def selectionSort(A):
    n = len(A)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if A[min] > A[j]:
                min = j
        print(A, i, j)
        A[i], A[min] = A[min], A[i]



if __name__ == '__main__':
    A = [23, 42, 4, 16, 8, 15]
    selectionSort(A)
    print(A)
