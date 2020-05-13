import pytest
from pytest import approx

import maidenhead


def test_latlon2maiden(location):
    m = maidenhead.toMaiden(*location.latlon)
    assert m == location.maiden[:6]


def test_maiden2latlon(location):
    lat, lon = maidenhead.toLoc(location.maiden)
    assert lat == approx(location.latlon[0], rel=0.0001)
    assert lon == approx(location.latlon[1], rel=0.0001)


@pytest.mark.parametrize(
    "latlon, maiden",
    [(mcmurdo, "RB32id27"), (washington_monument, "FM18lv53"), (giza_pyramid, "KL59nx65")],
)
def test_maiden2latlon(latlon, maiden):
    lat, lon = maidenhead.toLoc(maiden)
    assert lat == approx(latlon[0], rel=0.0001)
    assert lon == approx(latlon[1], rel=0.0001)


if __name__ == "__main__":
    pytest.main(["-x", __file__])
