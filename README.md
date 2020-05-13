# Maidenhead &lt;-&gt; Lat/Lon

[![DOI](https://zenodo.org/badge/132653071.svg)](https://zenodo.org/badge/latestdoi/132653071)
![Actions Status](https://github.com/space-physics/maidenhead/workflows/ci/badge.svg)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/space-physics/maidenhead.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/space-physics/maidenhead/context:python)
[![pypi versions](https://img.shields.io/pypi/pyversions/maidenhead.svg)](https://pypi.python.org/pypi/maidenhead)
[![PyPi Download stats](http://pepy.tech/badge/maidenhead)](http://pepy.tech/project/maidenhead)

`maidenhead` provides a simple, yet effective location hashing
algorithm. Maidenhead allows global location precision down to 750m

Maidenhead provides 4 levels of increasing accuracy

  Level |  Precision
--------|------------
  1     |  World
  2     |  Regional
  3     |  Metropolis
  4     |  City

## Install

```sh
pip install maidenhead
```

or for development version

```sh
git clone https://github.com/space-physics/maidenhead

pip install -e maidenhead
```

## Examples

All examples assume first doing

```python
import maidenhead as mh
```

### lat lon to Maidenhead locator

```python
mh.to_maiden(lat, lon, level)
```

returns a char (len = lvl*2)

### Maidenhead locator to lat lon

```python
mh.to_location('AB01cd')
```

take any string and returns topleft lat, lon of Maidenhead grid square.

## Command Line

Python:

```sh
python Maidenhead.py 65 -148
```

## Alternatives

We also have
[Maidenhead conversion for Julia](https://github.com/space-physics/maidenhead-julia).

Open Location Codes a.k.a Plus Codes are in
[Python code by Google](https://github.com/google/open-location-code/tree/master/python).