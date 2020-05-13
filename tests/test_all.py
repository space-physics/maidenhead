import pytest
import maidenhead
from pytest import approx

# Fixed points that can be used for testing
mcmurdo = (-77.8419, 166.6863)
washington_monument = (38.8895, -77.0353)
giza_pyramid = (29.9792, 31.1342)


@pytest.mark.parametrize(
    "latlon, maiden",
    [(mcmurdo, "RB32id27"), (washington_monument, "FM18lv53"), (giza_pyramid, "KL59nx65")],
)
def test_latlon2maiden(latlon, maiden):
    m = maidenhead.toMaiden(*latlon)
    assert m == maiden[:6]


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
