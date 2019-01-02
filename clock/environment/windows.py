from abc import ABC, abstractmethod
from tkinter import Tk


class Window(ABC):
    """Represent abstraction of an environment window."""

    @property
    @abstractmethod
    def root(self) -> Tk:
        """Return root of a window content."""
        pass

    @abstractmethod
    def set_title(self, name: str) -> None:
        """Set title of a window."""
        pass

    @abstractmethod
    def start_loop(self, count: int = 0) -> None:
        """Start main loop of a window."""
        pass

    @abstractmethod
    def stop_loop(self) -> None:
        """Stop main loop of a window."""
        pass


class ClockMaster(Window):
    """The class represents root ui window of a clock."""

    def __init__(self, screen_name=None, base_name=None, class_name='Tk', use_tk=1, sync=0, use=None) -> None:
        self._master: Tk = Tk(
            screenName=screen_name,
            baseName=base_name,
            className=class_name,
            useTk=use_tk,
            sync=sync,
            use=use
        )

    @property
    def root(self) -> Tk:
        return self._master

    def set_title(self, name: str) -> None:
        self._master.title(name)

    def start_loop(self, count: int = 0) -> None:
        self._master.mainloop(count)

    def stop_loop(self) -> None:
        self._master.quit()
