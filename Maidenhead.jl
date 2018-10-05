#!/usr/bin/env julia

using Test

function toMaiden(lat::Real, lon::Real; precision::Int=3)
    #Returns a maidenloc for specified lat-lon tuple at specified level.

  a = divrem(lon+180, 20)
  b = divrem(lat+90, 10)

  astring = string(Char('A' + Int(a[1])), Char('A'+ Int(b[1])))
  lon = a[2] / 2.
  lat = b[2]
  i = 1

  while i < precision
    i += 1
    a = divrem(lon, 1)
    b = divrem(lat, 1)

    if (i % 2) == 0
      astring *= string(Int(a[1])) * string(Int(b[1]))
      lon = 24 * a[2]
      lat = 24 * b[2]
    else
      astring *= string('A' + Int(a[1]), 'A' + Int(b[1]))
      lon = 10 * a[2]
      lat = 10 * b[2]
    end
  end

  if length(astring) >= 6
    astring = astring[1:4] * lowercase(astring[5:6]) * astring[7:end]
  end

  return astring

end


function toLoc(maiden::String)

    maiden = uppercase(maiden)

    N = length(maiden)

    Oa = Char('A')
    lon = -180.
    lat = -90.
# %% first pair
    lon += (Char(maiden[1])-Oa)*20
    lat += (Char(maiden[2])-Oa)*10
# %% second pair
    if N >= 4
        lon += parse(Int, maiden[3])*2
        lat += parse(Int, maiden[4])*1
    end
    if N >= 6
        lon += (Char(maiden[5])-Oa) * 5.0/60
        lat += (Char(maiden[6])-Oa) * 2.5/60
    end
    if N >= 8
        lon += parse(Int, maiden[7]) * 5.0/600
        lat += parse(Int, maiden[8]) * 2.5/600
    end
    
    return (lat, lon)
end


if basename(PROGRAM_FILE) == basename(@__FILE__)

  if length(ARGS) == 2
    println(toMaiden(ARGS[1], ARGS[2], precision=3))
  elseif length(ARGS) == 1
    println(toLoc(ARGS[1]))
  else
    @test toMaiden(40, -50) == "GN50aa"
  
    lat, lon = toLoc("JO32ii09")
    @test isapprox(lat, 52.37083333333334)
    @test isapprox(lon, 6.666666666666667)
  end
end
