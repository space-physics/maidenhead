#!/usr/bin/env python
import unittest
import maidenhead

# Fixed points that can be used for testing
casa_henri = (52.3726967, 6.6725457)
eiffel_tower = (48.8583094, 2.2945333)


class BasicTests(unittest.TestCase):
    def test_nonsense(self):
        """Test no.nonsense.ee/qthmap"""
        m = maidenhead.toMaiden(casa_henri)
        u = maidenhead.genNonSense(casa_henri,4)
        self.assertEqual(u,'http://no.nonsense.ee/qthmap/?qth=JO32ii09')


    def test_is_sane(self):
        """Test toMaiden"""
        m = maidenhead.toMaiden(casa_henri)
        self.assertEqual(m,"JO32ii")

    def test_genmap(self):
        """Test level maps are different"""
        m = maidenhead.toMaiden(casa_henri,3)
        g = maidenhead.genGoogleMap(m)
        m1 = maidenhead.toMaiden(casa_henri,2)
        g1 = maidenhead.genGoogleMap(m1)
        self.assertNotEqual(g,g1)

    def test_decimals(self):
        lat, lon = maidenhead.toLoc('JO32ii09')
        self.assertEqual(lat, 52.37083333333334)
        self.assertEqual(lon, 6.666666666666667)


if __name__ == '__main__':
    unittest.main()
