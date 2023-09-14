from __future__ import annotations
import argparse
from copy import copy

import maidenhead


def main(
    loc: str | tuple[float, float],
    precision: int = 6,
    url: bool = False,
    center: bool = False,
) -> str | tuple[float, float]:

    if isinstance(loc, str):  # maidenhead
        maiden = copy(loc)
        loc = maidenhead.to_location(loc, center)
        print(f"{loc[0]:.7f} {loc[1]:.7f}")
    elif len(loc) == 2:  # lat lon
        if isinstance(loc[0], str):
            loc = (float(loc[0]), float(loc[1]))
        maiden = maidenhead.to_maiden(*loc, precision=precision)
        print(maiden)
        loc = maiden
    else:
        raise ValueError("specify Maidenhead grid (single string) or lat lon (with space between)")

    if url:
        uri = maidenhead.google_maps(maiden, center)
        print(uri)
        return uri

    return loc


p = argparse.ArgumentParser(description="convert to / from Maidenhead locator")
p.add_argument(
    "loc", help="Maidenhead grid (single string) or lat lon (with space between)", nargs="+"
)
p.add_argument("-p", "--precision", help="maidenhead precision", type=int, default=3)
p.add_argument("--url", help="also output Google Maps URL", action="store_true")
p.add_argument(
    "-c",
    "--center",
    help="output lat lon of the center of provided maidenhead grid square "
    "(default output: lat lon of it's south-west corner)",
    action="store_true",
)
args = p.parse_args()

if len(args.loc) == 1:
    loc = args.loc[0]
else:
    loc = args.loc

main(loc, args.precision, args.url, args.center)
