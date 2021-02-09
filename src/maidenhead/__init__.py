"""
Maidenhead grid conversion <==> latitude, longitude

toMaiden([lat, lon], level) returns a char (len = lvl*2)
toLoc(mloc) takes any string and returns topleft [lat,lon] within mloc

Beyond 8 characters is not defined for Maidenhead.
"""

from .to_location import to_location
from .to_maiden import to_maiden


def google_maps(maiden: str, center: bool = False) -> str:
    """
    generate Google Maps URL from Maidenhead grid

    Parameters
    ----------

    maiden : str
        Maidenhead grid

    center : bool
        If true, return the center of provided maidenhead grid square, instead of default south-west corner

    Results
    -------

    url : str
        Google Maps URL
    """

    loc = to_location(maiden, center)

    url = f"https://www.google.com/maps/@?api=1&map_action=map&center={loc[0]},{loc[1]}"

    return url
