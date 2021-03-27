def selection_sort(A):
    print("SELECTION SORT STARTED ON", A, "\n")

    for i in range(len(A)):
        m = i
        print("Currently, A =", A, " idx m =", m)

        for j in range(i, len(A)):
            print("\tChecking j = ", j)
            if A[m] >= A[j]:
                m = j
            print("\tm =", m)

        print("\tmin idx at m =", m)

        A[m], A[i] = A[i], A[m]

    print("FINAL SORTED A: ", A, "\n")


def insertion_sort(A):
    print("INSERTION SORT STARTED ON", A, "\n")
    for i in range(1, len(A)):
        j = i
        print("Currently, A =", A, " idx j =", j)

        while j > 0 and A[j] < A[j - 1]:
            print("\tWhoop! j = ", j, "and", A[j],"<", A[j - 1] )

            A[j - 1], A[j] = A[j], A[j - 1]
            j = j - 1
            print("\tswap done: A =", A, "and now j =", j)

    print("FINISHED:", A, "\n")

def merge_sort(A, a = 0, b = None):     # Sort sub-array A[a:b]
    if b is None:
        b = len(A)      

    if 1 < b - a:                       # O(1) size k = b - a
        c = (a + b + 1) // 2
        merge_sort(A, a, c)             # sort left
        merge_sort(A, a, c)             # sort right

        L, R = A[a:c], A[c:b]           # copy

        i, j = 0, 0 
        while a < b:                    # O(n)
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):   # O(1) check side
                A[a] = L[i]             # O(1) merge from left
                i = i + 1               # decrement left pointer
            else:
                A[a] = R[j]             # O(1) merge from right
                j = j + 1               # decrement right pointer
            
            a = a + 1                   # decrement merge pointer


if __name__ == "__main__":
    test = [5, -2, 12, 3, 11]

    merge_sort(test)
    print(test)