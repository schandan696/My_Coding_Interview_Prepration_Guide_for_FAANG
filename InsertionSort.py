'''
Algorithm for Insertion Sort
'''

def selectionSort(A):
    n = len(A)
    for i in range(1,n):
        j = i-1
        temp = A[i]
        while(j >= 0 and A[j] > temp):
            print(A, i, j)
            A[j+1] = A[j]
            j -= 1
        A[j] = temp
        #print(A, i, j)
        #A[i], A[j] = A[j], A[i]





if __name__ == '__main__':
    A = [23, 42, 4, 16, 8, 15]
    selectionSort(A)
    print(A)
