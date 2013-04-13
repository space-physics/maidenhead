import unittest
import mlocs

# Fixed points that can be used for testing
casa_henri = (52.3726967, 6.6725457)
eiffel_tower = (48.8583094, 2.2945333)


class BasicTests(unittest.TestCase):
    def test_mloc_nonsense(self):
        """Test no.nonsense.ee/qthmap"""
        m = mlocs.toMaiden(casa_henri)
        u = mlocs.genNonSense(casa_henri,4)
	self.assertEquals(u,'http://no.nonsense.ee/qthmap/?qth=JO32II09')


    def test_mloc_is_sane(self):
        """Test toMaiden"""
        m = mlocs.toMaiden(casa_henri)
        self.assertEquals(m,"JO32II09")

    def test_mloc_6_is_precise(self):
        """Test toMaiden(6) on own maiden"""
        m = mlocs.toMaiden(casa_henri,6)
        l = mlocs.toLoc(m)
        n = mlocs.toMaiden(l,6)
        self.assertEquals(n,m)
	
    def test_mloc_genmap(self):
        """Test level maps are different"""
        m = mlocs.toMaiden(casa_henri,5)
        g = mlocs.genGoogleMap(m)
        m1 = mlocs.toMaiden(casa_henri,4)
        g1 = mlocs.genGoogleMap(m1)
        self.assertNotEquals(g,g1)


if __name__ == '__main__':
    unittest.main()
