======================================
mlocs: Maidenhead <-> Lat/Lon
======================================

``mlocs`` provides a simple, yet effective location hashing algorithm.
Maidenhead allows global location precision down to 750m 


Maidenhead provides 5 levels of increasing accuracy

========  =========
Level     Precision
========  =========
1          World 
2          Regional
3          Metropolis
4          City
5          Neighborhood
========  =========

Install
=======
::

    python setup.py develop

Examples
=========
::
    
    mlocs.toMaiden([lat, lon], level) 

returns a char (len = lvl*2)

::

    mlocs.toLoc(mloc) 

take any string and returns topleft [lat,lon] within Maidenhead grid.

