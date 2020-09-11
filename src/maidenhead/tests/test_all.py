import pytest
from pytest import approx

import maidenhead


def test_latlon2maiden(location):
    m = maidenhead.to_maiden(*location.latlon)
    assert m == location.maiden[:6]


def test_maiden2latlon(location):
    lat, lon = maidenhead.to_location(location.maiden)
    assert lat == approx(location.latlon[0], rel=0.0001)
    assert lon == approx(location.latlon[1], rel=0.0001)


@pytest.mark.parametrize("invalid", [None, 1, True, False])
def test_invalid_maiden(invalid):
    with pytest.raises(AttributeError):
        maidenhead.to_location(maiden=invalid)


def test_invalid_maiden_len():
    with pytest.raises(ValueError):
        maidenhead.to_location(maiden="GG52qjjjjj")
