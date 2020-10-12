import pytest

from maidenhead.__main__ import main


def test_convert_maiden_to_loc():
    assert main((27, 34)) == "KL77aa"


def test_convert_loc_to_maiden():
    assert main("GG52qj") == pytest.approx([-27.6250, -48.6667])


@pytest.mark.parametrize("args_str", ["GG52qj", (-27.625, -48.66666666)])
def test_render_maps_url(args_str):
    assert (
        main(args_str, url=True)
        == "https://www.google.com/maps/@?api=1&map_action=map&center=-27.625,-48.666666666666664"
    )
