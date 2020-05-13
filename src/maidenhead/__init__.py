from typing import Tuple

"""
Maidenhead grid conversion <==> latitude, longitude

toMaiden([lat, lon], level) returns a char (len = lvl*2)
toLoc(mloc) takes any string and returns topleft [lat,lon] within mloc

Beyond 8 characters is not defined for Maidenhead.
"""


def to_location(maiden: str) -> Tuple[float, float]:
    """
    convert Maidenhead grid to latitude, longitude

    Parameters
    ----------

    maiden : str
        Maidenhead grid locator of length 2 to 8

    Returns
    -------

    latLon : tuple of float
        Geographic latitude, longitude
    """
    if not isinstance(maiden, str):
        raise TypeError("Maidenhead locator must be a string")

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

    return lat, lon


def to_maiden(lat: float, lon: float = None, *, precision: int = 3) -> str:
    """
    Returns a maidenhead string for latitude, longitude at specified level.

    Parameters
    ----------

    lat : float or tuple of float
        latitude or tuple of latitude, longitude
    lon : float, optional
        longitude (if not given tuple)
    precision : int, optional
        level of precision (length of maidenhead grid string output)

    Returns
    -------

    maiden : str
        Maidenhead grid string of specified precision
    """

    A = ord("A")
    a = divmod(lon + 180, 20)
    b = divmod(lat + 90, 10)
    maiden = chr(A + int(a[0])) + chr(A + int(b[0]))
    lon = a[1] / 2.0
    lat = b[1]
    i = 1
    while i < precision:
        i += 1
        a = divmod(lon, 1)
        b = divmod(lat, 1)
        if not (i % 2):
            maiden += str(int(a[0])) + str(int(b[0]))
            lon = 24 * a[1]
            lat = 24 * b[1]
        else:
            maiden += chr(A + int(a[0])) + chr(A + int(b[0]))
            lon = 10 * a[1]
            lat = 10 * b[1]

    if len(maiden) >= 6:
        maiden = maiden[:4] + maiden[4:6].lower() + maiden[6:]

    return maiden


def google_maps(maiden: str) -> str:
    """
    generate Google Maps URL from Maidenhead grid

    Parameters
    ----------

    maiden : str
        Maidenhead grid

    Results
    -------

    url : str
        Google Maps URL
    """

    latlon = to_location(maiden)

    url = "https://www.google.com/maps/@?api=1&map_action=map" "&center={},{}".format(
        latlon[0], latlon[1]
    )

    return url


toLoc = to_location
toMaiden = to_maiden
