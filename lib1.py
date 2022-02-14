import math

def sumacplx(c1,c2):

    return (c1[0] + c2[0], c1[1] + c2[1])

def multiplicacioncplx(c1,c2):

    real = ((c1[0] * c2[0]) - (c1[1] * c2 [1]))
    imaginario = ((c1[0] * c2[1]) + (c2[0] * c1[1]))

    return (real, imaginario)

def divisioncplx(c1, c2):

    real = ((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    imaginario = ((c1[1] * c2[0]) - (c1[0] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))

    return (real, imaginario)

def conjugadocplx(c1):

    return (c1[0], (- c1[1]))

def modulocplx(c1):

    return (((c1[0] ** 2) + (c1[1] ** 2)) ** (1/2))

def restacplx(c1, c2):

    return (c1[0] - c2[0], c1[1] - c2[1])

def cartesianas_a_polarescplx(c1,P,Teta):

    p = math.sqrt((((c1[0]) ** 2) + (c1[1] ** 2)))
    teta = math.atan((c1[1] / c1[0]))

    a = (P * math.cos(Teta))
    b = (P * math.sin(Teta))

    return (p, teta),(a,b)

def fasecplx(c1):

    teta = math.atan((c1[1] / c1[0]))

    return teta


if __name__ == '__main__':


    print(modulocplx((1,-1)))
    print(multiplicacioncplx((3,-1), (1,4)))
    print(divisioncplx((4,6), (7,9)))
    print(cartesianas_a_polarescplx((1,1), (3),(3.1416/4)))
    print(fasecplx((1,1)))
    print(conjugadocplx((2,3)))
    print(restacplx((1,2), (5,9)))
    print(sumacplx([1,2],[5,6]))