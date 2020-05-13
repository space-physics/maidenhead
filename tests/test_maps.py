import pytest
import maidenhead as mh

mcmurdo = (-77.8419, 166.6863)
washington_monument = (38.8895, -77.0353)
giza_pyramid = (29.9792, 31.1342)


@pytest.mark.parametrize(
    "latlon, maiden",
    [(mcmurdo, "RB32id27"), (washington_monument, "FM18lv53"), (giza_pyramid, "KL59nx65")],
)
def test_GoogleMaps(latlon, maiden):
    m = mh.toMaiden(*latlon, precision=4)
    assert m == maiden
    g4 = mh.google_maps(m)

    m1 = mh.toMaiden(*latlon)
    assert m1 == maiden[:6]
    g1 = mh.google_maps(m1)
    assert g4 != g1
