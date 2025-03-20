###########################TP1###########################
def prodmat(A,B):
    if(len(A[0]) != len(B)):
        raise ValueError("Wrong size of matrix")
    else:
        C = []

        for i in range (len(A)):
            line = []
            for j in range (len(B[0])):
                value = 0 
                for k in range (len(B)):
                    value += A[i][k] * B[k][j]
                line.append(value)
            C.append(line)
        return C

def printMatrix(A):
    for i in range (len(A)):
        for j in range (len(A[i])):
            print(str(A[i][j]) + " ", end=" ")
        print ('\n')


def deter(A):
    n = len(A)
    if (n == 1):
        return A[0][0]
    
    det = 0
    for j in range (n):
        subMatrix =[]
        for i in range (1,n):
            subRow = []
            for k in range (n):
                if (k!=j):
                    subRow.append(A[i][k])
            subMatrix.append(subRow)
        det += (-1)**(0+j) * A[0][j] * deter(subMatrix)
    return det

def com(A):
    comMatrix = []
    for i in range (len(A)):
        comRow = []
        for j in range (len(A[0])):
            subMatrix = []
            for k in range (len(A)):
                subRow = []
                if (k!=i):
                    for l in range (len(A[0])):
                        if (l!=j):
                            subRow.append(A[k][l])
                    subMatrix.append(subRow)
            comRow.append((-1)**(i+j)* deter(subMatrix))
        comMatrix.append(comRow)
    return comMatrix

def tran(A):
    returnMatrix = []
    for i in range (len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        returnMatrix.append(row)
    return returnMatrix

def multiplyScalarWithMatrix(scalar, A):
    M = []
    for i in range (len(A)):
        row = []
        for j in range (len(A[0])):
            row.append(A[i][j] * scalar)
        M.append(row)
    return M

def inverse(A):
    DetA = deter(A)
    if DetA == 0:
        raise ValueError("Det Matrix equal 0")
    return multiplyScalarWithMatrix(1/DetA, tran(com(A)))


M = [[1,2,3],[45,67,12],[0,9,0]]

#printMatrix(inverse(M))

