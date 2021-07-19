program test_maidenhead

use maidenhead

real(real64) :: lat, lon
character(8) :: buf
integer :: i, L

call get_command_argument(1, buf, length=L, status=i)
if(L>8 .or. L<2) error stop "Maidenhead locator 2-8 characters"
if (i/=0) then
  error stop "please provide a Maidenhead locator"
endif

call maiden2latlon(buf, .true., lat, lon)

print *, lat, lon

end program
