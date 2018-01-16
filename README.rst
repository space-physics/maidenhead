.. image:: https://travis-ci.org/scivision/maidenhead.svg?branch=master
    :target: https://travis-ci.org/scivision/maidenhead
    
.. image:: https://coveralls.io/repos/github/scivision/maidenhead/badge.svg?branch=master
    :target: https://coveralls.io/github/scivision/maidenhead?branch=master

.. image:: https://api.codeclimate.com/v1/badges/6ac63c6a3ec7a22c3d87/maintainability
   :target: https://codeclimate.com/github/scivision/maidenhead/maintainability
   :alt: Maintainability

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

    pip install -e .

Examples
=========
::
    
    maidenhead.toMaiden([lat, lon], level) 

returns a char (len = lvl*2)

::

    maidenhead.toLoc('AB01cd') 

take any string and returns topleft [lat,lon] of Maidenhead grid square.

Command Line
-------------------
Python::

    ./Maidenhead.py 65 -148
    
    
Julia::

    ./Maidenhead.jl 65 -148

