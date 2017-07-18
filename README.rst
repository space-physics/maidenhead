.. image:: https://travis-ci.org/scivision/maidenhead.svg?branch=master
    :target: https://travis-ci.org/scivision/maidenhead

======================================
Maidenhead <-> Lat/Lon
======================================

``maidenhead`` provides a simple, yet effective location hashing algorithm.
Maidenhead allows global location precision down to 750m 


Maidenhead provides 4 levels of increasing accuracy

========  =========
Level     Precision
========  =========
1          World 
2          Regional
3          Metropolis
4          City
========  =========

Install
=======
::

    python setup.py develop

Examples
=========
::
    
    maidenhead.toMaiden([lat, lon], level) 

returns a char (len = lvl*2)

::

    maidenhead.toLoc('AB01cd') 

take any string and returns topleft [lat,lon] of Maidenhead grid square.

