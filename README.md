[![image](https://travis-ci.org/scivision/maidenhead.svg?branch=master)](https://travis-ci.org/scivision/maidenhead)
[![image](https://coveralls.io/repos/github/scivision/maidenhead/badge.svg?branch=master)](https://coveralls.io/github/scivision/maidenhead?branch=master)
[![Build status](https://ci.appveyor.com/api/projects/status/4b44p65o33088top?svg=true)](https://ci.appveyor.com/project/scivision/maidenhead)
[![pypi versions](https://img.shields.io/pypi/pyversions/maidenhead.svg)](https://pypi.python.org/pypi/maidenhead)
[![pypi format](https://img.shields.io/pypi/format/maidenhead.svg)](https://pypi.python.org/pypi/maidenhead)
[![PyPi Download stats](http://pepy.tech/badge/maidenhead)](http://pepy.tech/project/maidenhead)

# Maidenhead &lt;-&gt; Lat/Lon

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

    pip install -e .

## Examples
All examples assume first doing
```python
import maidenhead as mh
```
   
### lat lon to Maidenhead locator
```python
mh.toMaiden([lat, lon], level) 
```
returns a char (len = lvl*2)

### Maidenhead locator to lat lon
```python
mh.toLoc('AB01cd') 
```
take any string and returns topleft [lat, lon] of Maidenhead grid square.

## Command Line

Python:

    Maidenhead.py 65 -148

Julia:

    ./Maidenhead.jl 65 -148
