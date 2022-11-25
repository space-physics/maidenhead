program main

use, intrinsic :: iso_fortran_env, only : real64
use maidenhead, only : maiden2latlon

implicit none

real(real64) :: lat, lon
character(8) :: buf1
integer :: i, L

i = command_argument_count()

select case (i)
case (1)
  call get_command_argument(1, buf1, length=L, status=i)
  if(L>8 .or. L<2) error stop "Maidenhead locator 2-8 characters"
  if (i/=0) error stop "please provide a Maidenhead locator"


  call maiden2latlon(buf1, .true., lat, lon)
  print '(2F9.4)', lat, lon

case default
  error stop "give Maidenhead locator string OR latitude longitude"
end select

end program
