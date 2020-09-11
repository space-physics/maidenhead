import argparse

import maidenhead


def main():
    p = argparse.ArgumentParser(description="convert to / from Maidenhead locator")
    p.add_argument(
        "loc", help="Maidenhead grid (single string) or lat lon (with space between)", nargs="+"
    )
    p.add_argument("-p", "--precision", help="maidenhead precision", type=int, default=3)
    p.add_argument("-u", "--url", help="also output Google Maps URL", action="store_true")
    args = p.parse_args()

    if len(args.loc) == 1:  # maidenhead
        maiden = args.loc[0]
        print('{:.4f} {:.4f}'.format(*maidenhead.to_location(maiden)))
    elif len(args.loc) == 2:  # lat lon
        maiden = maidenhead.to_maiden(*map(float, args.loc), precision=args.precision)
        print(maiden)
    else:
        raise SystemExit("specify Maidenhead grid (single string) or lat lon (with space between)")

    if args.url:
        print(maidenhead.google_maps(maiden))
