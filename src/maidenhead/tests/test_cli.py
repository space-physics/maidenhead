import pytest
import subprocess


def test_convert_maiden_to_loc():
    ret = subprocess.check_output(["maidenhead", "27", "34"], universal_newlines=True)

    assert ret.strip() == "KL77aa"


def test_convert_loc_to_maiden():
    ret = subprocess.check_output(["maidenhead", "GG52qj"], universal_newlines=True)

    assert ret.strip() == "-27.625 -48.666666666666664"


def test_invalid_loc_args():
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output(["maidenhead", "GG52qj", "27.34", "23.98"])


@pytest.mark.parametrize("args_str", ["GG52qj", "-27.625 -48.66666666"])
def test_render_maps_url(args_str):
    args = args_str.split()
    args.append("-u")
    ret = subprocess.check_output(["maidenhead"] + args, universal_newlines=True)
    L = ret.split("\n")

    assert (
        L[1]
        == "https://www.google.com/maps/@?api=1&map_action=map&center=-27.625,-48.666666666666664"
    )
