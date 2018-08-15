#!/usr/bin/env python
import pytest
import maidenhead
from pytest import approx

# Fixed points that can be used for testing
casa_henri = (52.3726967, 6.6725457)
eiffel_tower = (48.8583094, 2.2945333)


def test_nonsense():
    """Test no.nonsense.ee/qthmap"""
    m = maidenhead.toMaiden(casa_henri)
    assert m == 'JO32ii'

    u = maidenhead.genNonSense(casa_henri, 4)
    assert u == 'http://no.nonsense.ee/qthmap/?qth=JO32ii09'


def test_is_sane():
    """Test toMaiden"""
    m = maidenhead.toMaiden(casa_henri)
    assert m == "JO32ii"


def test_genmap():
    """Test level maps are different"""
    m = maidenhead.toMaiden(casa_henri, 3)
    g = maidenhead.genGoogleMap(m)
    m1 = maidenhead.toMaiden(casa_henri, 2)
    g1 = maidenhead.genGoogleMap(m1)
    assert g != g1


def test_decimals():
    lat, lon = maidenhead.toLoc('JO32ii09')
    assert lat == approx(52.37083333333334)
    assert lon == approx(6.666666666666667)


if __name__ == '__main__':
    pytest.main(['-x', __file__])
