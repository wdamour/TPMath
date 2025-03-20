import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import pi
from math import sqrt

def pave_plein(n,a,b,c,x0,y0,z0):
    X = []
    Y = []
    Z = []
    k = int(n**(1/3))
    if (n != k**3):
        k+=1
    dx =  a / (k - 1)
    dy =  b / (k - 1)
    dz =  c / (k - 1)
    #8 points de base
    X.extend([x0,x0,x0,x0,a+x0,a+x0,a+x0,a+x0])
    Y.extend([y0,y0,b+y0,b+y0,y0,y0,b+y0,b+y0])
    Z.extend([z0,c+z0,z0,c+z0,z0,c+z0,z0,c+z0])
    count = 8
    for i in range(k):
        for j in range(k):
            for l in range(k):
                if count < n:  
                    #Testing if it's not the base value
                    if (i == 0):
                        if (j == 0):
                            if (l == 0 or l == k):
                                break;
                        elif(j == k):
                            if (l == 0 or l == k):
                                break;
                    elif (i == k):
                        if (j == 0):
                            if (l == 0 or l == k):
                                break;
                        elif(j == k):
                            if (l == 0 or l == k):
                                break;   
                    #end of testing
                    X.append(x0 + i * dx)
                    Y.append(y0 + j * dy)
                    Z.append(z0 + l * dz)
                    count += 1
                else:
                    break
            if count >= n:
                break
        if count >= n:
            break
    return X, Y, Z

def plot_list_points(X,Y,Z):
    if (len(X) != len(Y) and len(X) != len(Z)):
        raise ValueError("Not the same amount of coordiantes")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(X[0], Y[0], Z[0], c='b', marker='o')
    for i in range(1,len(X)):
        ax.scatter(X[i], Y[i], Z[i], c='r', marker='o')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.show()
    
#X, Y, Z = pave_plein(1000, 10, 10, 10, 0, 0, 0)
#plot_list_points(X, Y, Z)

def factoriel(n):
    if(n<0 or (isinstance(n, int)) == False):
       raise ValueError("can calculate factorial of negative number or a non-int") 
    if (n==0):
        return 1
    return n*factoriel(n-1)

def cosinus(x):
    cos = 0
    k = 0
    term = ((-1)**k) * ((x ** (2*k))/(factoriel(2*k)))
    max_terms = 20 
    while (abs(term) > 1e-10 and k < max_terms):
        cos += term
        k += 1
        term  = ((-1)**k) * ((x ** (2*k))/(factoriel(2*k)))
    return cos

def sinus(x):
    sin = 0
    k = 0
    term = ((-1)**k) * ((x ** (2*k+1))/(factoriel(2*k+1)))
    max_terms = 20 
    while (abs(term) > 1e-10 and k < max_terms):
        sin += term
        k += 1
        term  = ((-1)**k) * ((x ** (2*k+1))/(factoriel(2*k+1)))
    return sin

def cercle_plein(R,x0,y0,z0, n, maxOutercircle=6):
    #on cap le nombre de points sur l'exterieur du cercle à 6 (arbitraire)
    X,Y,Z = [],[],[]
    X.append(x0)
    Y.append(y0)
    Z.append(z0)
    count = 1
    baseAngle = 2*pi
    nb_angle = 0
    if (n-1<=maxOutercircle):
        baseAngle /= (n-1)
        nb_angle = (n-1)
    else :
        baseAngle /= maxOutercircle
        nb_angle = maxOutercircle
    nb_r = 1
    if (n>maxOutercircle+1):
        nb_r = (n-1) // maxOutercircle
        if ((n-1) % maxOutercircle != 0):
            nb_r += 1
    r = R / nb_r
    for i in range(1,nb_r + 1):
        for j in range (nb_angle):
            if (count >= n):
                break
            X.append(x0 + r*i * cosinus(baseAngle*j))
            Y.append(y0 + r*i * sinus(baseAngle*j))
            Z.append(z0)
            count +=1
        if (count >= n):
                break
    return X,Y,Z

def cylindre_plein(R,h,x0,y0,z0,n,nb_h,maxOutercircle=6):
    X,Y,Z=[],[],[]
    h_variation = h / nb_h
    nb_circle = n//nb_h
    for i in range (nb_h):
        x,y,z = cercle_plein(R,x0,y0,z0+h_variation*i, nb_circle, maxOutercircle)
        X.extend(x)
        Y.extend(y)
        Z.extend(z)
    return X,Y,Z
        
    

X, Y, Z = cylindre_plein(5, 5,0, 0, 0,100, 4)
plot_list_points(X, Y, Z)

    