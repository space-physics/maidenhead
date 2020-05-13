import pytest

import maidenhead
from maidenhead.cli import main


@pytest.fixture
def maps_url_spy(mocker):
    return mocker.spy(maidenhead, "google_maps")


@pytest.fixture
def to_location_spy(mocker):
    return mocker.spy(maidenhead, "to_location")


@pytest.fixture
def to_maiden_spy(mocker):
    return mocker.spy(maidenhead, "to_maiden")


def test_convert_maiden_to_loc(to_location_spy, to_maiden_spy):
    main(["27", "34"])

    assert 0 == to_location_spy.call_count
    assert 1 == to_maiden_spy.call_count


def test_convert_loc_to_maiden(to_location_spy, to_maiden_spy):
    main(["GG52qj"])

    assert 1 == to_location_spy.call_count
    assert 0 == to_maiden_spy.call_count


def test_invalid_loc_args(to_location_spy, to_maiden_spy):
    main("GG52qj 27.34 23.98".split())

    assert 0 == to_location_spy.call_count
    assert 0 == to_maiden_spy.call_count


@pytest.mark.parametrize("args_str", ["GG52qj", "27.2 29.0"])
def test_render_maps_url(args_str, maps_url_spy):
    args = args_str.split()
    args.append("-u")
    main(args)

    assert 1 == maps_url_spy.call_count
