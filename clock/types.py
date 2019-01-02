from abc import ABC, abstractmethod


class Runner(ABC):
    """Abstract interface for some runner."""

    @abstractmethod
    def perform(self) -> None:
        """Start some option to perform."""
        pass
