import lib1 as lc



def adicionvectores(v, w):
    n = len(v)
    r = []
    for k in range(n):
        r += [lc.sumacplx(v[k], w[k])]
    return r



def inversovector(v):
    n = len(v)
    r = []
    for k in range(n):
        r += [lc.multiplicacioncplx((-1, 0), v[k])]
    return r



def multiplicacionescalarvector(v, w):
    n = len(w)
    r = []
    for k in range(n):
        r += [lc.multiplicacioncplx(v, w[k])]
    return r



def adicionmatrices(A, B):
    for row in range(len(A)):
        B[row] = adicionvectores(A[row], B[row])
    return B





def inversaditivamatrices(v):
    m = len(v)
    n = len(v[0])
    r = [n] * m
    for j in range(m):
        fila = []
        r[j] = fila
        for k in range(n):
            r[j] += [lc.multiplicacioncplx((-1,0), v[j][k])]
    return r



def multiplicacionescalarmatriz(v, w):
    m = len(w)
    n = len(w[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [lc.multiplicacioncplx(v, w[j][k])]
    return r



def transpuestamatrixvector(v):
    m = len(v)
    n = len(v[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [v[k][j]]
    return r



def conjugadamatriz(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = lc.conjugadocplx(A[i][j])

    return A


def adjuntamatriz(A):

    matrizad = conjugadamatriz(transpuestamatrixvector(A))

    return matrizad


def productomatrices(A, B):
    m = len(A)
    n = len(A[0])
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):
        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.multiplicacioncplx(A[j][k], B[j][k])
    return r



def matrizVector(A,V):

    if len(A[0]) == len(V):
        accion = []
        for i in range(len(A)):
            accion.append((0, 0))
        for i in range(len(A)):
            for j in range(len(V)):
                for k in range(len(A[0])):
                    accion[i] = lc.sumacplx(accion[i], lc.multiplicacioncplx(A[i][k], V[j]))
        return accion
    else:
        return False


def productointernovectores(v1,v2):
    if len(v1) == len(v2):
        productoint = (0, 0)
        vectorc1 = conjugadov(v1)
        for i in range(len(v1)):
            productoint = lc.sumacplx(productoint, lc.multiplicacioncplx(v1[i], v2[i]))

        return productoint
    else:
        return False


def normavector(v):
    r = int(lc.modulocplx(v))
    return r


def distanciavectores(v,w):
    ele = 0
    s = 0
    for i in range(len(v)):
        ele = v[i]-w[i]
        ele = ele**2
        s += ele
    n = s ** (1/2)
    return n

def matrizunitaria(matriz):
    matrizt = adjuntamatriz(matriz)
    identidad = [[(0, 0) for i in range(len(matriz[0]))] for j in range(len(matriz))]
    for i in range(len(identidad)):
        for j in range(len(identidad[0])):
            if i == j:
                identidad[i][j] = (1, 0)
    if productomatrices(matrizt, matriz) == identidad:
        return True
    else:
        return False




def matrizhermitiana(v):

    if adjuntamatriz(v) == v:

        return True
    else:

        return False



def productotensormatrices(A, B):
    na = len(A)
    nb = len(B)
    nr = nb * na
    R = [(0, 0)] * nr
    index = 0
    for j in range(na):
        for k in range(nb):
            R[index] = multiplicacionescalarvector(A[j], B[k])
            index = index + 1
    return R

def conjugadov(lista):

    for i in range(len(lista)):
        lista[i] = lc.conjugadocplx(lista[i])
    return lista


if __name__ == '__main__':

    print(adicionmatrices([[(1, 1), (2, 2)], [(3, 3), (4, 4)]], [[(1, 1), (2, 2)], [(3, 3), (4, 4)]]))
    print(conjugadamatriz([[(1, 0), (2, 3)], [(4, 5), (1, 0)]]))
    print(matrizVector([[(2, -1), (4, 1)], [(8, -6), (7, 6)]], [(4.0, -1.8), (9.0, 3.0)]))
    print(productointernovectores([(1, 0), (2, 3)], [(4, 5), (1, 0)]))
    print(normavector([3,5,8,1,1]))
    print(matrizunitaria([[(1, 1), (2, 2)], [(3, 3), (4, 4)]]))
    print(matrizhermitiana([[(1, 1), (2, 2)], [(3, 3), (4, 4)]]))

