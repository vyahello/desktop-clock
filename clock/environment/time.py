from abc import ABC, abstractmethod
from time import strftime


class Time(ABC):
    """Abstract interface for a time."""

    @abstractmethod
    def as_string(self) -> str:
        """Return time as a string."""
        pass


class ClockTime(Time):
    """Interface represents clock time."""

    def __init__(self, fmt: str = '%H:%M:%S') -> None:
        self._fmt = fmt

    def as_string(self) -> str:
        return strftime(self._fmt)
