#!/usr/bin/env python
import maidenhead
from argparse import ArgumentParser
import sys


def main():
    p = ArgumentParser()
    p.add_argument('loc', help='Maidenhead grid or lat lon', nargs='+')
    p.add_argument('-p', '--precision', help='maidenhead precision', type=int, default=3)
    p.add_argument('-u', '--url', help='also output Google Maps URL', action='store_true')
    p = p.parse_args()

    if len(p.loc) == 1:  # maidenhead
        maiden = p.loc[0]
        lat, lon = maidenhead.toLoc(maiden)
        print(lat, lon)
    elif len(p.loc) == 2:  # lat lon
        maiden = maidenhead.toMaiden(p.loc[0], p.loc[1], p.precision)
        print(maiden)
    else:
        print('specify Maidenhead grid (single string) or lat lon (with space between)', file=sys.stderr)

    if p.url:
        print(maidenhead.google_maps(maiden))


if __name__ == '__main__':
    main()
