import itertools
import operator
import functools


def to_maiden(lat: float, lon: float, precision: int = 3) -> str:
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

    # The QTH locator encoding can be treated as a mixed radix integer number.
    # The floating point values will be converted into integers by applying
    # a multiplier that is chosen based on the required level of precision
    # in order to retain accuracy.

    # Do the conversion according to radix starting from right most position
    # returns a generaror  which produce values for each position (from least to most significant)
    # I.e in reverse order.
    def convert(val, radix):
        while radix:
            p, q = divmod(val, radix[-1])
            base = ord("a") if len(radix) == 3 else ord("A")
            yield str(q) if radix[-1] == 10 else chr(q + base)
            val = p
            radix = radix[:-1]

    def float_coord_to_fixed_scale(f, shift, max_val, multiplier):
        scale = 10**12
        n, d = f.as_integer_ratio()
        fixed = ((n + shift * d) * scale + d // 2) // d
        max_val_scaled = max_val * scale
        if fixed != max_val_scaled:
            fixed %= max_val_scaled

        res = (multiplier * fixed) // max_val_scaled
        return min(max(0, res), multiplier - 1)

    radix = [18] + [24 if i % 2 else 10 for i in range(precision - 1)]
    multiplier = functools.reduce(operator.mul, radix)

    int_lat = float_coord_to_fixed_scale(lat, 90, 180, multiplier)
    int_lon = float_coord_to_fixed_scale(lon, 180, 360, multiplier)

    maiden = "".join(reversed(list(itertools.chain(*zip(convert(int_lat, radix), convert(int_lon, radix))))))

    return maiden
