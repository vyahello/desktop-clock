from pyats import aetest
from time import strftime
from clock.time import Time, ClockTime


@aetest.loop(time_format=[
    '%H:%M:%S',
    '%I:%M:%S%p',
    '%A, %B %d %Y'
],
    result=[
        strftime('%H:%M:%S'),
        strftime('%I:%M:%S%p'),
        strftime('%A, %B %d %Y')
    ])
class TestClockTime(aetest.Testcase):
    @aetest.setup
    def setup(self, time_format: str):
        self.parameters['clock'] = ClockTime(time_format)

    @aetest.test
    def test(self, clock: Time, result: str) -> None:
        assert clock.as_string() == result


if __name__ == '__main__':
    aetest.main()
