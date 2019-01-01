from pyats import aetest
from tkinter import Tk
from typing import Tuple
from clock.widgets import PurpleUIWidget

_font: Tuple[str, int, str] = (
    'times',
    300,
    'bold'
)
_back_ground: str = 'purple'


class TestPurpleUIWidget(aetest.Testcase):
    @aetest.setup
    def setup(self) -> None:
        self.parameters['widget'] = PurpleUIWidget(Tk())

    @aetest.test
    def test_font(self, widget: PurpleUIWidget) -> None:
        assert widget._font == _font

    @aetest.test
    def test_back_ground(self, widget: PurpleUIWidget) -> None:
        assert widget._back_ground == _back_ground
