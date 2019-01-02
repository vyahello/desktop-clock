from abc import ABC, abstractmethod
from clock.environment.engines import Engine, ClockEngine
from clock.environment.time import Time, ClockTime
from clock.environment.widgets import Widget, PurpleUIWidget
from clock.environment.windows import Window
from clock.types import Runner


class Clock(ABC):
    """Represent abstraction of clock."""

    @abstractmethod
    def start(self) -> None:
        """Start running a clock."""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Stop running a clock."""
        pass


class DigitalClock(Clock):
    """Unified digital clock."""

    def __init__(self, name: str, time: Time, master: Window, widget: Widget) -> None:
        self._name = name
        self._master = master
        self._widget = widget
        self._engine: Engine = ClockEngine(time, widget)

    def start(self) -> None:
        self._master.set_title(self._name)
        self._engine.run()
        self._master.start_loop()

    def stop(self) -> None:
        self._master.stop_loop()


class PurpleDigitalClock(Clock):
    """Represent concrete purple digital clock."""

    def __init__(self, master: Window, name: str) -> None:
        self._clock: Clock = DigitalClock(
            name=name,
            time=ClockTime(),
            master=master,
            widget=PurpleUIWidget(master)
        )

    def start(self) -> None:
        self._clock.start()

    def stop(self) -> None:
        self._clock.stop()


class ClockRunner(Runner):
    """Main clock runner."""

    def __init__(self, clock: Clock) -> None:
        self._clock: Clock = clock

    def perform(self):
        """Start the clock functioning."""
        self._clock.start()
