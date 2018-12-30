from time import strftime
import pytest
from clock.time import Time, ClockTime


@pytest.mark.parametrize("time_format, result", [
    ('%H:%M:%S', strftime('%H:%M:%S')),
    ('%I:%M:%S%p', strftime('%I:%M:%S%p')),
    ('%A, %B %d %Y', strftime('%A, %B %d %Y'))
])
def test_time(time_format: str, result: str) -> None:
    time: Time = ClockTime(time_format)
    assert time.as_string() == result
