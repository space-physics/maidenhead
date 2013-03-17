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

def toHor(mloc):
	"""Returns mloc encoded east-west value
	"""
	pick = True
	res = ""

	for i in range(mloc.__len__()):
		if pick:
			res += mloc[i]
			pick = False
		else:
			pick = True
	return res

def toVer(mloc):
	"""Returns mloc encoded north-south value
	"""
	pick = False
	res = ""

	for i in range(mloc.__len__()):
		if pick:
			res += mloc[i]
			pick = False
		else:
			pick = True
	return res

def create(hor,ver):
	"""Returns an mloc from [h1,h2,h3],[v1,v2,v3]
	as [h1,v1,h2,v2,h3,v3]
	"""
	res = ""
	assert(hor.__len__() == ver.__len__())
	for i in range(hor.__len__()):
		res += hor[i]
		res += ver[i]
	return res

def minus(mloc):
	# from right to left (lol)
	for i in range(mloc.__len__(), 0):
		if(isdigit(mloc[i])


def left(mloc):
	"""Returns the mloc to the left (west) of mloc
	It move along horizontal (toHor) axis.
	"""
	h = toHor(mloc)
	v = toVer(mloc)

	n = h - 1

	return create(n,v)

