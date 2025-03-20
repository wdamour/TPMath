###########################TP2###########################
import TP1
def prodvect(u,v):
    return [u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]

def moment(F,A,G):
    V = [G[0]-A[0], G[1]-A[1], G[2]-A[2]]
    return prodvect(V,F)

def solve1(f,fp,h):
    return f+fp*h

def translation(m, h, F, G, v):
    a = [F[0]/m, F[1]/m, F[2]/m]
    newV = [solve1(v[0], a[0], h), solve1(v[1], a[1], h), solve1(v[2], a[2], h)]
    newPos = [solve1(G[0], v[0], h), solve1(G[1], v[1], h), solve1(G[2], v[2], h)]
    return newPos, newV

def rotation(h,F,A,G,I,teta,tetap):
    SommeMoment = []
    X = 0
    Y = 0
    Z = 0
    for i in range (len(F)):
        MomentValue = moment(F[i], A[i], G)
        X += MomentValue[0]
        Y += MomentValue[1]
        Z += MomentValue[2]
    SommeMoment.extend([X,Y,Z])
    Omega = TP1.prodmat(TP1.inverse(I),SommeMoment)
    newTetap = [solve1(tetap[0], Omega[0], h), solve1(tetap[1], Omega[1], h),solve1(tetap[2], Omega[2], h)]
    newTeta = [solve1(teta[0], newTetap[0], h), solve1(teta[1], newTetap[1], h),solve1(teta[2], newTetap[2], h)]
    return newTeta, newTetap


