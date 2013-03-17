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

if __name__ == '__main__':
    unittest.main()
