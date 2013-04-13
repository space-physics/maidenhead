# mlocs - sensible location storage...
# 
# mlocs provides a simple, yet effective location hashing algorithm.
# it's not super precise (> 750m.) but it provides perfect results.
#
# There are 5 levels available.
# Lvl 1 : World Scope
# Lvl 2 : Region Scope
# Lvl 3 : Metro Scope
# Lvl 4 : City Scope
# Lvl 5 : I See You
#
# toMaiden([lat, lon], level) returns a char (len = lvl*2)
# toLoc(mloc) takes any string and returns topleft [lat,lon] within mloc

Version 1.0.3 :
===============
Addedd genNonSense(loc) for other map :)

Version 1.0.2 :
===============
Added genGooleMap() for generating static google-map images out of MLOCS :)
  --> for large scale (>25k req/day) these *must* be cached somehow....


