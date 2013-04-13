"""## mlocs - sensible location storage...
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
"""
import math
import random
import re,string
def f(z):
    """Used in the toLoc-function. That's about all I can tell ya :)
    """
    return 10**(-(z-1)/2)*24**(-z/2) 
	#this is my stroke of genius or something

def toLoc(maiden):
    """Takes any(!) maidenloc (<22) and returns 
    a location tupel [lat,lon]
    """
    A = ord('A')
    lon = -90
    lat = -90
    lets=re.findall(r'([A-Xa-x])([A-Xa-x])', maiden) 
    nums=re.findall(r'(\d)(\d)', maiden)
    i = 0
    tot = 0
    val = range(0,len(lets)+len(nums))
    for m in val:
        val[m] = None
    for x,y in lets:
        val[i*2]=(ord(string.upper(x))-A,ord(string.upper(y))-A)
        i += 1
        tot += 1
    i = 0
    for x,y in nums:
        val[i*2+1]=(string.atoi(x),string.atoi(y))
        i += 1
        tot += 1
    i = 0
    for x,y in val[0:len(lets)+len(nums)]:
        lon += f(i-1) * x
        lat += f(i-1) * y
        i += 1
    lon *= 2
    return [lat,lon]

def toMaiden(position, precision=4):
    """Returns a maidenloc for specified lat-lon tupel at specified 
    level. (4 being the default)
    """
    lat = position[0]
    lon = position[1]
    A = ord('A')
    a = divmod(lon+180, 20)
    b = divmod(lat+90, 10)
    astring = chr(A+int(a[0])) + chr(A+int(b[0]))
    lon = a[1]/2
    lat = b[1]
    i = 1
    while i < precision:
        i += 1
        a = divmod(lon,1)
        b = divmod(lat,1)
        if not (i%2):
            astring += str(int(a[0])) + str(int(b[0]))
            lon = 24 * a[1]
            lat = 24 * b[1]
        else:
            astring += chr(A+int(a[0])) + chr(A+int(b[0]))
            lon = 10 * a[1]
            lat = 10 * b[1]


    return astring

def genGoogleMap(mloc=""):
	if mloc:
		position = toLoc(mloc)
		strout = "http://maps.googleapis.com/maps/api/staticmap?"
		strout += "center=" + str(position[0])
		strout += "," + str(position[1])
		strout += "&zoom=10&size=320x240&sensor=false"
		return strout
	
def genNonSense(loc, level=3):
	lat = loc[0]
	lon = loc[1]
	mloc = toMaiden([lat,lon],level)
	return "http://no.nonsense.ee/qthmap/?qth=" + mloc
		
