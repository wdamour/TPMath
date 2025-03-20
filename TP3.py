def centre_inert(L):
    X = 0
    Y = 0
    Z = 0
    for point in L:
        X += point[0]
        Y += point[1]
        Z += point[2]
    n = len(L)
    return [X/n, Y/n, Z/n]

def matrice_inert(L,m):
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    for point in L:
        A += point[1]**2 + point[2]**2
        B += point[0]**2 + point[2]**2
        C += point[0]**2 + point[1]**2

        D += point[1]*point[2]
        E += point[0]*point[2]
        F += point[0]*point[1]
    return [[A*m, -F*m, -E*m],[-F*m, B*m, -D*m],[-E*m, -D*m, C*m]]

def AddMatrixes(A,B):
    if(len(A) != len(B) or len(A[0]) != len(B[0])):
                raise ValueError("Matrixes of different size")
    MatTotal = []
    for i in range (len(A)):
        Row = []
        for j in range (len(A[0])):
            Row.append(A[i][j]+B[i][j])
        MatTotal.append(Row)
    return MatTotal
        

def deplace_matrice(I,m,O,A):
    OA = [A[0]-O[0], A[1]-O[1], A[2]-O[2]]
    mat = [
        [m*((OA[1]**2)+(OA[2]**2)), -m*OA[0]*OA[1], -m*OA[0]*OA[2]],
        [-m*OA[0]*OA[1], m*((OA[0]**2)+(OA[2]**2)), -m*OA[1]*OA[2]],
        [-m*OA[0]*OA[2], -m*OA[1]*OA[2], m*((OA[0]**2)+(OA[1]**2))],
    ]
    return AddMatrixes(I,mat)
