#!/usr/bin/env python
import maidenhead
from argparse import ArgumentParser, Namespace


def cmdparse() -> Namespace:
    p = ArgumentParser()
    p.add_argument('loc', help='Maidenhead grid or lat lon', nargs='+')
    p.add_argument('-p', '--precision', help='maidenhead precision', type=int, default=3)
    return p.parse_args()


def main(p: Namespace):
    if len(p.loc) == 1:  # maidenhead
        lat, lon = maidenhead.toLoc(p.loc[0])
        print(lat, lon)
    elif len(p.loc) == 2:  # lat lon
        loc = maidenhead.toMaiden(p.loc, p.precision)
        print(loc)
    else:
        raise TypeError('specify Maidenhead grid (single string) or lat lon (with space between)')


if __name__ == '__main__':
    main(cmdparse())
