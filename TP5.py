import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import TP1
import TP2
import TP3
import TP4

def mouvement(W,m,I,G,v,teta,tetap,F,A,h):
    sommeF = [0,0,0]
    for i in range (len(F)):
        sommeF[0] += F[i][0]
        sommeF[1] += F[i][1]
        sommeF[2] += F[i][2]
        
    newG, newv = TP2.translation(m, h, sommeF, G, v)
    newteta, newtetap = TP2.rotation(h, F, A, G, I, teta, tetap)
    
    newW = []
    X,Y,Z = [],[],[]
    for i in range (len(W[0])):
        new_point = [
            W[0][i] + (newG[0]-G[0]),
            W[1][i] + (newG[1]-G[1]),
            W[2][i] + (newG[2]-G[2]),
        ]

        omega = TP2.prodvect(newteta, [W[0][i] - G[0], W[1][i] - G[1], W[2][i] - G[2]])
        X.append(new_point[0] + omega[0] * h)
        Y.append(new_point[1] + omega[1] * h)
        Z.append(new_point[2] + omega[2] * h)
        
    newW.append(X)
    newW.append(Y)
    newW.append(Z)
    return newW, newG, newv, newteta, newtetap

def trace_mouvements(W, m, I, G, v, teta, tetap, F, A, h, t, n):
    dt = t / n  

    positions = []

    W_current = W
    G_current = G
    v_current = v
    teta_current = teta
    tetap_current = tetap

    for _ in range(n):
        W_current, G_current, v_current, teta_current, tetap_current = mouvement(
            W_current, m, I, G_current, v_current, teta_current, tetap_current, F, A, dt
        )
        positions.append(W_current)
        
    for i in range(n):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        X = positions[i][0]
        Y = positions[i][1]
        Z = positions[i][2]
        ax.scatter(X, Y, Z, c='r', marker='o')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f"Position à t={round(i * dt, 2)}s")


        # Assurez-vous que les axes ont la même échelle
        max_range = max(
            max(X) - min(X), 
            max(Y) - min(Y), 
            max(Z) - min(Z)
        )
        
        # Ajuster les limites de chaque axe pour avoir une même échelle
        mid_x = (max(X) + min(X)) / 2
        mid_y = (max(Y) + min(Y)) / 2
        mid_z = (max(Z) + min(Z)) / 2

        ax.set_xlim(mid_x - max_range / 2, mid_x + max_range / 2)
        ax.set_ylim(mid_y - max_range / 2, mid_y + max_range / 2)
        ax.set_zlim(mid_z - max_range / 2, mid_z + max_range / 2)

        ax.set_box_aspect([1, 1, 1]) 
        plt.show()
        
cylindre = TP4.cylindre_plein(5,10,0,0,0,500,5, 10)
m = 10
I = TP3.matrice_inert(cylindre, m)
G = TP3.centre_inert(cylindre)
v = [1,-2,3]
teta = [1,3,0]
tetap = [1,1,1]
F = [[0,0,-100],[100,0,0]]
trace_mouvements(cylindre, m, I, G, v, teta, tetap, F, [G], 2, 1, 5)