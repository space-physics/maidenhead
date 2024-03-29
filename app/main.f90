program main

use maidenhead, only : to_location, to_maiden, wp

implicit none

real(wp) :: lat, lon
character(8) :: buf1, buf2
integer :: i, L

i = command_argument_count()

select case (i)
case (1)
  call get_command_argument(1, buf1, length=L, status=i)
  if(L>8 .or. L<2) error stop "Maidenhead locator 2-8 characters"
  if (i/=0) error stop "please provide a Maidenhead locator"


  call to_location(buf1, .true., lat, lon)
  print '(2F9.4)', lat, lon
case (2)
  call get_command_argument(1, buf1, status=i)
  if (i/=0) error stop "please provide lat lon"
  call get_command_argument(2, buf2, status=i)
  if (i/=0) error stop "please provide lat lon"

  read(buf1, *) lat
  read(buf2, *) lon

  call to_maiden(lat, lon, buf2)
  print '(a8)', buf2
case default
  error stop "give Maidenhead locator string OR latitude longitude"
end select

end program
