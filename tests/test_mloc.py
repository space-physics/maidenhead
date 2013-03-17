import unittest
import mlocs

# Fixed points that can be used for testing
casa_henri = (52.3726967, 6.6725457)
eiffel_tower = (48.8583094, 2.2945333)


class BasicTests(unittest.TestCase):

    def test_mloc_is_sane(self):
        """Test toMaiden"""
        m = mlocs.toMaiden(casa_henri)
        pass

    def test_mloc_6_is_precise(self):
        """Test toMaiden(6) on own maiden"""
        m = mlocs.toMaiden(casa_henri,6)
        l = mlocs.toLoc(m)
        n = mlocs.toMaiden(l,6)
        self.assertEquals(n,m)

    def test_mloc_toHor(self):
        """get east-west value for mloc"""
        m = mlocs.toMaiden(casa_henri,6)
        l = mlocs.toHor(m)
        self.assertEquals(l,"J3I0Q9")

    def test_mloc_toVer(self):
        """get north-south value for mloc"""
        m = mlocs.toMaiden(casa_henri,6)
        l = mlocs.toVer(m)
        self.assertEquals(l,"O2I9K7")

    def test_mloc_left(self):
        """Test left on own maiden"""
        m = mlocs.toMaiden(casa_henri,5)
        l = mlocs.left(m)
        self.assertEquals(l,m)

if __name__ == '__main__':
    unittest.main()
