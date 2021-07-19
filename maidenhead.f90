module maidenhead

use, intrinsic :: iso_fortran_env, only : real64

implicit none (type, external)

contains

elemental subroutine maiden2latlon(maiden, center, lat, lon)
!! convert Maidenhead grid to latitude, longitude
!!
!! Parameters
!! ----------

!! maiden : str
!!     Maidenhead grid locator of length 2 to 8

!! center : bool
!!     If true, return the center of provided maidenhead grid square, instead of default south-west corner
!!     Default value = False needed to maidenhead full backward compatibility of this module.

!! Returns
!! -------

!! lat : float
!!     Geographic latitude
!! lon : float
!!     Geographic longitude


character(*), intent(in) :: maiden
logical, intent(in) :: center
real(real64), intent(out) :: lon, lat

character(8) :: maid
integer :: N, Oa
integer :: j, i

maid = toUpper(maiden)

N = len_trim(maiden)
if(modulo(N, 2) /= 0) error stop "Maidenhead locator requires even number of characters"
if(N < 2 .or. N > 8) error stop "Maidenhead locator requires 2-8 characters"

Oa = iachar("A")
lon = -180.0
lat = -90.0

!> first pair
lon = lon + (iachar(maid(1:1)) - Oa) * 20
lat = lat + (iachar(maid(2:2)) - Oa) * 10
!> second pair
if (N >= 4) then
  read(maid(3:3), '(I1)', iostat=i) j
  if(i/=0) error stop "expect integers as 3rd and 4th values"
  lon = lon + j * 2
  read(maid(4:4), '(I1)', iostat=i) j
  if(i/=0) error stop "expect integers as 3rd and 4th values"
  lat = lat + j * 1
endif
!> third pair
if (N >= 6) then
  lon = lon + (iachar(maid(5:5)) - Oa) * 5.0 / 60
  lat = lat + (iachar(maid(6:6)) - Oa) * 2.5 / 60
endif
!> fourth pair
if (N >= 8) then
  read(maid(7:7), '(I1)', iostat=i) j
  if(i/=0) error stop "expect integers as 7th and 8th values"
  lon = lon + j * 5.0 / 600
  read(maid(8:8), '(I1)') j
  if(i/=0) error stop "expect integers as 7th and 8th values"
  lat = lat + j * 2.5 / 600
endif

!> move lat lon to the center (if requested)
if(center) then
  select case (N)
  case(2)
    lon = lon + 20 / 2
    lat = lat + 10 / 2
  case(4)
    lon = lon + 2 / 2
    lat = lat + 1.0 / 2
  case(6)
    lon = lon + 5.0 / 60 / 2
    lat = lat + 2.5 / 60 / 2
  case(8)
    lon = lon + 5.0 / 600 / 2
    lat = lat + 2.5 / 600 / 2
  case default
    error stop "maidenhead locator requires 2, 4, 6, or 8 characters"
  end select
endif

end subroutine maiden2latlon


elemental function toUpper(str)
!! ASCII letters to uppercase
character(*), intent(in) :: str
character(len(str)) :: toUpper
character(*), parameter :: lower="abcdefghijklmnopqrstuvwxyz", &
                            upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
integer :: i,j

toUpper = str

!do concurrent (i = 1:len(str))  ! FIXME: Flang
do i = 1,len(str)
  j = index(lower,str(i:i))
  if (j > 0) toUpper(i:i) = upper(j:j)
end do

end function toUpper

end module maidenhead
