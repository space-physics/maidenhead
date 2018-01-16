#!/usr/bin/env julia

using ArgParse

function toMaiden(lat, lon; precision=3)
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



s = ArgParseSettings()
@add_arg_table s begin
    "lat"
        help = "latitude"
        arg_type = Float64
        required = true
    "lon"
        help = "longitude"
        arg_type = Float64
        required = true
end
s = parse_args(s)

maiden = toMaiden(s["lat"], s["lon"], precision=3)

println(maiden)
