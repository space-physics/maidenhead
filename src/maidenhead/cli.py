import sys
from argparse import ArgumentParser

import maidenhead


def fetch(input_args):
    p = ArgumentParser()
    p.add_argument(
        "loc", help="Maidenhead grid (single string) or lat lon (with space between)", nargs="+"
    )
    p.add_argument("-p", "--precision", help="maidenhead precision", type=int, default=3)
    p.add_argument("-u", "--url", help="also output Google Maps URL", action="store_true")
    return p.parse_args(input_args)


def main(input_args):
    args = fetch(input_args)

    if len(args.loc) == 1:  # maidenhead
        maiden = args.loc[0]
        lat, lon = maidenhead.to_location(maiden)
        print(lat, lon)
    elif len(args.loc) == 2:  # lat lon
        maiden = maidenhead.to_maiden(
            lat=float(args.loc[0]), lon=float(args.loc[1]), precision=args.precision
        )
        print(maiden)
    else:
        print(
            "specify Maidenhead grid (single string) or lat lon (with space between)",
            file=sys.stderr,
        )

    if args.url:
        print(maidenhead.google_maps(maiden))


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
