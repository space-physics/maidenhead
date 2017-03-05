======================================
mlocs: Maidenhead <-> Lat/Lon
======================================

``mlocs`` provides a simple, yet effective location hashing algorithm.
Maidenhead allows global location precision down to 750m 


Maidenhead provides 5 levels of increasing accuracy
Lvl 1 : World Scope
Lvl 2 : Region Scope
Lvl 3 : Metro Scope
Lvl 4 : City Scope
Lvl 5 : I See You

Examples
=========
::
    
    toMaiden([lat, lon], level) 

returns a char (len = lvl*2)

::

    toLoc(mloc) 

take any string and returns topleft [lat,lon] within Maidenhead grid.

