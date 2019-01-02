from abc import ABC
from clock.environment.time import Time
from clock.environment.widgets import Widget


class Engine(ABC):
    """Represent abstract interface for an engine that runs clock continuously."""

    _ms_to_continue: int = 100

    def run(self) -> None:
        """Run the engine."""
        pass


class ClockEngine(Engine):
    """Represent engine that runs clock continuously."""

    def __init__(self, time: Time, widget: Widget) -> None:
        self._time = time
        self._widget = widget

    def run(self) -> None:
        self._widget.create_grid()
        self._widget.configure(self._time.as_string())
        self._widget.continue_after(self._ms_to_continue, self.run)
