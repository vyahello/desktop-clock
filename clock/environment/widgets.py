from abc import ABC, abstractmethod
from tkinter import Tk, Label
from typing import Callable, Tuple


class Widget(ABC):
    """Represent abstraction of an environment widget."""

    @abstractmethod
    def create_grid(self) -> None:
        """Create grid of content."""
        pass

    @abstractmethod
    def configure(self, text: str) -> None:
        """Configure resources of a widget."""
        pass

    @abstractmethod
    def continue_after(self, ms: int, option: Callable) -> None:
        """Continue running a function after certain time stamp."""
        pass


class UIWidget(Widget):
    """Represent gui widget of a digital clock."""

    def __init__(self, master: Tk, font: Tuple[str, int, str], back_ground: str) -> None:
        self._widget = Label(master, font=font, bg=back_ground)

    def create_grid(self) -> None:
        self._widget.grid()

    def configure(self, text: str) -> None:
        self._widget.config(text=text)

    def continue_after(self, ms: int, option: Callable) -> None:
        self._widget.after(ms, option)


class PurpleUIWidget(Widget):
    """Represent purple gui widget of a digital clock."""

    _font: Tuple[str, int, str] = (
        'times',
        300,
        'bold'
    )
    _back_ground: str = 'purple'

    def __init__(self, master: Tk) -> None:
        self._widget: Widget = UIWidget(master, self._font, self._back_ground)

    def create_grid(self) -> None:
        self._widget.create_grid()

    def configure(self, text: str) -> None:
        self._widget.configure(text)

    def continue_after(self, ms: int, option: Callable) -> None:
        self._widget.continue_after(ms, option)
