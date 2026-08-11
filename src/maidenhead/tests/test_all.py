import pytest
from pytest import approx

import maidenhead


def test_latlon2maiden(location):
    m = maidenhead.to_maiden(*location.latlon)
    assert m == location.maiden[:6]


def test_precision(location_precision):
    assert location_precision.maiden[:2] == maidenhead.to_maiden(*location_precision.latlon, precision=1)
    assert location_precision.maiden[:4] == maidenhead.to_maiden(*location_precision.latlon, precision=2)
    assert location_precision.maiden[:6] == maidenhead.to_maiden(*location_precision.latlon, precision=3)
    assert location_precision.maiden[:8] == maidenhead.to_maiden(*location_precision.latlon, precision=4)
    assert location_precision.maiden[:10] == maidenhead.to_maiden(*location_precision.latlon, precision=5)
    assert location_precision.maiden[:12] == maidenhead.to_maiden(*location_precision.latlon, precision=6)


def test_maiden2latlon(location):
    lat, lon = maidenhead.to_location(location.maiden)
    assert lat == approx(location.latlon[0], rel=0.0001)
    assert lon == approx(location.latlon[1] if location.latlon[1] <= 180 else location.latlon[1] - 360, rel=0.0001)


@pytest.mark.parametrize("invalid", [None, 1, True, False])
def test_invalid_maiden(invalid):
    with pytest.raises(AttributeError):
        maidenhead.to_location(maiden=invalid)


def test_invalid_maiden_len():
    with pytest.raises(ValueError):
        maidenhead.to_location(maiden="GG52qjjjjj")
