import typing as T


def to_location(maiden: str, center: bool = False) -> T.Tuple[float, float]:
    """
    convert Maidenhead grid to latitude, longitude

    Parameters
    ----------

    maiden : str
        Maidenhead grid locator of length 2 to 8

    center : bool
        If true, return the center of provided maidenhead grid square, instead of default south-west corner
        Default value = False needed to maidenhead full backward compatibility of this module.

    Returns
    -------

    latLon : tuple of float
        Geographic latitude, longitude
    """

    maiden = maiden.strip().upper()

    N = len(maiden)
    if not 8 >= N >= 2 and N % 2 == 0:
        raise ValueError("Maidenhead locator requires 2-8 characters, even number of characters")

    Oa = ord("A")
    lon = -180.0
    lat = -90.0
    # %% first pair
    lon += (ord(maiden[0]) - Oa) * 20
    lat += (ord(maiden[1]) - Oa) * 10
    # %% second pair
    if N >= 4:
        lon += int(maiden[2]) * 2
        lat += int(maiden[3]) * 1
    # %%
    if N >= 6:
        lon += (ord(maiden[4]) - Oa) * 5.0 / 60
        lat += (ord(maiden[5]) - Oa) * 2.5 / 60
    # %%
    if N >= 8:
        lon += int(maiden[6]) * 5.0 / 600
        lat += int(maiden[7]) * 2.5 / 600

    # %% move lat lon to the center (if requested)
    if center:
        if N == 2:
            lon += 20 / 2
            lat += 10 / 2
        elif N == 4:
            lon += 2 / 2
            lat += 1.0 / 2
        elif N == 6:
            lon += 5.0 / 60 / 2
            lat += 2.5 / 60 / 2
        elif N >= 8:
            lon += 5.0 / 600 / 2
            lat += 2.5 / 600 / 2

    return lat, lon
