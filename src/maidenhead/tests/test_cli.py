import pytest
import sys
import subprocess


def test_convert_maiden_to_loc():
    ret = subprocess.check_output([sys.executable, "-m", "maidenhead", "27", "34"], text=True)
    assert ret.strip() == "KL77aa"


def test_convert_loc_to_maiden():
    ret = subprocess.check_output([sys.executable, "-m", "maidenhead", "GG52qj"], text=True)
    loc = list(map(float, ret.strip().split()))
    assert loc == pytest.approx([-27.6250, -48.6667])


@pytest.mark.parametrize("args", [["GG52qj"], ["-27.625", "-48.66666666"]])
def test_render_maps_url(args):
    cmd = [sys.executable, "-m", "maidenhead"]
    cmd.extend(args)
    cmd.append("--url")
    print(cmd)
    ret = subprocess.check_output(cmd, text=True)

    assert (
        ret.strip().split("\n")[1]
        == "https://www.google.com/maps/@?api=1&map_action=map&center=-27.625,-48.666666666666664"
    )
