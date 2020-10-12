import argparse
import typing as T
from copy import copy

import maidenhead


def main(loc: T.Union[str, T.Sequence[float]], precision: int = 3, url: bool = False):
    if isinstance(loc, str):  # maidenhead
        maiden = copy(loc)
        loc = maidenhead.to_location(loc)
        print(f"{loc[0]:.4f} {loc[1]:.4f}")
    elif len(loc) == 2:  # lat lon
        if isinstance(loc[0], str):
            loc = list(map(float, loc))
        maiden = maidenhead.to_maiden(*loc, precision=precision)
        print(maiden)
        loc = maiden
    else:
        raise ValueError("specify Maidenhead grid (single string) or lat lon (with space between)")

    if url:
        uri = maidenhead.google_maps(maiden)
        print(uri)
        return uri

    return loc


def cli():
    p = argparse.ArgumentParser(description="convert to / from Maidenhead locator")
    p.add_argument(
        "loc", help="Maidenhead grid (single string) or lat lon (with space between)", nargs="+"
    )
    p.add_argument("-p", "--precision", help="maidenhead precision", type=int, default=3)
    p.add_argument("-u", "--url", help="also output Google Maps URL", action="store_true")
    args = p.parse_args()

    if len(args.loc) == 1:
        loc = args.loc[0]
    else:
        loc = args.loc

    main(loc, args.precision, args.url)


if __name__ == "__main__":
    cli()
