import lib2 as lc
from math import sqrt
import unittest

class Testlibreria2cplx(unittest.TestCase):

    def test_adicionveectores(self):
        suma = lc.adicionvectores([(1, -2.5), (2, 1)], [(3, 0), (7, -3.8)])
        self.assertEqual(suma, [(4, -2.5), (9, -2.8)])

    def test_inversovector(self):
        invAd = lc.inversovector([(6, -4), (7, 3)])
        self.assertEqual(invAd, [(-6, 4), (-7, -3)])

    def test_multiplicacionescalarvector(self):
        Msv = lc.multiplicacionescalarvector((3, 2), [(6, 3), (5, 1)])
        self.assertEqual(Msv, [(12, 21), (13, 13)])

    def test_adicionmatrices(self):
        sumatx = lc.adicionmatrices([[(1, 1), (2, 2)], [(3, 3), (4, 4)]], [[(1, 1), (2, 2)], [(3, 3), (4, 4)]])
        self.assertEqual(sumatx, [[(2, 2), (4, 4)], [(6, 6), (8, 8)]])

    def test_inversaditivamatrices(self):
        InvAdM = lc.inversaditivamatrices([[(4, 3), (2, 1)], [(9, 8), (7, 5)]])
        self.assertEqual(InvAdM, [[(-4, -3), (-2, -1)], [(-9, -8), (-7, -5)]])

    def test_multiplicacionescalarmatriz(self):
        MultEscMtx = lc.multiplicacionescalarmatriz((3, 2), [[(6, 3), (5, 1)], [(0, 0), (4, 0)]])
        self.assertEqual(MultEscMtx, [[(12, 21), (13, 13)], [(0, 0), (12, 8)]])

    def test_transpuestamatrizvector(self):
        trMt = lc.transpuestamatrixvector([[(1, 0), (2, 3)], [(4, 5), (1, 0)]])
        self.assertEqual(trMt, [[(1, 0), (4, 5)], [(2, 3), (1, 0)]])

    def test_conjugadamatriz(self):
        conjM = lc.conjugadamatriz([[(1, 0), (2, 3)], [(4, 5), (1, 0)]])
        self.assertEqual(conjM, [[(1, 0), (2, -3)], [(4, -5), (1, 0)]])

    def test_adjuntamatriz(self):
        HMt = lc.adjuntamatriz([[(6, -3), (2, 12), (0, -19)], [(0, 0), (5, 2.1), (17, 0)], [(1, 0), (2, 5), (3, -4.5)]])
        self.assertEqual(HMt, [[(6, 3), (0, 0), (1, 0)], [(2, -12), (5, -2.1), (2, -5)], [(0, 19), (17, 0), (3, 4.5)]])

    def test_productomatrices(self):
        PrMtx = lc.productomatrices([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]],[[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]])
        self.assertEqual(PrMtx,[[(26,-52),(60,24),(26,0)],[(9,7),(1,29),(14,0)],[(48,-21),(15,22),(20,22)]])

    def test_matrizVector(self):
        self.assertEqual(lc.matrizVector([[(2, -1), (4, 1)], [(8, -6), (7, 6)]], [(4.0, -1.8), (9.0, 3.0)]),[(78.0, 7.199999999999999), (195.0, 18.0)])

    def test_productointernovectores(self):
        self.assertEqual(lc.productointernovectores([(1, 0), (2, 3)], [(4, 5), (1, 0)]), (6, 2))

    def test_normavector(self):
        vNorm = lc.normavector([3,5,8,1,1])
        self.assertEqual(vNorm, 5)

    def test_distanciavectores(self):
        dv = lc.distanciavectores([3,1,2],[2,2,-1])
        self.assertEqual(dv, sqrt(11))

    def test_matrizunitaria(self):
        mu = lc.matrizunitaria([[(1, 1), (2, 2)], [(3, 3), (4, 4)]])
        self.assertEqual(mu, False)

    def test_matrizhermitiana(self):
        mh = lc.matrizhermitiana([[(1, 1), (2, 2)], [(3, 3), (4, 4)]])
        self.assertEqual(mh, False)

    def productotensormatrices(self):
        VTP = lc.productotensormatrices([3, 4, 7], [-1, 2])
        self.assertEqual(VTP, [-3, 6, -4, 8, -7, 14])




if __name__ == '__main__':
    unittest.main()
