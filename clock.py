from clock.clocks import PurpleDigitalClock, ClockRunner
from clock.environment.windows import ClockMaster
from clock.types import Runner


def _runner() -> Runner:
    """Start functioning the clock."""
    return ClockRunner(
        PurpleDigitalClock(
            name='Purple Desktop Digital Clock',
            master=ClockMaster()
        )
    )


if __name__ == '__main__':
    _runner().perform()
