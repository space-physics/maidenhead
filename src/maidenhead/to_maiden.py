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
