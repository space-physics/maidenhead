import maidenhead as mh


def test_googlemaps_precision(location):
    m = mh.to_maiden(*location.latlon, precision=4)
    assert m == location.maiden

    g4 = mh.google_maps(m)

    m1 = mh.to_maiden(*location.latlon)
    assert m1 == location.maiden[:6]

    g1 = mh.google_maps(m1)
    assert g4 != g1
