from __future__ import annotations


def to_location(maiden: str, center: bool = False) -> tuple[float, float]:
    """
    convert Maidenhead grid to latitude, longitude

    Parameters
    ----------

    maiden : str
        Maidenhead grid locator of length 2 to 12

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
    if not ((12 >= N >= 2) and (N % 2 == 0)):
        raise ValueError("Maidenhead locator requires 2-12 characters, even number of characters")

    Oa = ord("A")
    lon = -180.0
    lat = -90.0
    # cf. https://en.wikipedia.org/wiki/Maidenhead_Locator_System
    # cf. https://fastapi.metacpan.org/source/MEH/Ham-Locator-0.1000/lib/Ham/Locator.pm
    # cf. https://www.earthpoint.us/Convert.aspx
    # %% first pair
    lon += (ord(maiden[0]) - Oa) * 20
    lat += (ord(maiden[1]) - Oa) * 10
    # %% second pair
    if N >= 4:
        lon += int(maiden[2]) * 2
        lat += int(maiden[3]) * 1
    # %%
    if N >= 6:
        lon += (ord(maiden[4]) - Oa) * 0.0833333 # 5' in degrees
        lat += (ord(maiden[5]) - Oa) * 0.0416667 # 2.5' in degrees
    # %%
    if N >= 8:
        lon += int(maiden[6]) * 0.0083333 # 30" in degrees
        lat += int(maiden[7]) * 0.0041667 # 15" in degrees

    # %%
    if N >= 10:
        lon += (ord(maiden[8]) - Oa) * (0.0083333/24) # 30" / 24 in degrees
        lat += (ord(maiden[9]) - Oa) * (0.0041667/24) # 15" / 24 in degrees

    # %%
    if N >= 12:
        lon += int(maiden[10]) * (0.0083333/(24*10))
        lat += int(maiden[11]) * (0.0041667/(24*10))
        
    # %% move lat lon to the center (if requested)
    if center:
        if N == 2:
            lon += 20 / 2
            lat += 10 / 2
        elif N == 4:
            lon += 2 / 2
            lat += 1.0 / 2
        elif N == 6:
            lon += 0.0833333 / 2
            lat += 0.0416667 / 2
        elif N == 8:
            lon += 0.0083333 / 2
            lat += 0.0041667 / 2
        elif N == 10:
            lon += (0.0083333/24) / 2
            lat += (0.0041667/24) / 2
        elif N == 12:
            lon += (0.0083333/(24*10)) / 2
            lat += (0.0041667/(24*10)) / 2

    return lat, lon
