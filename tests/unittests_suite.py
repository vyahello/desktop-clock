import os
from pyats import easypy
from typing import Set


_tests_dir_path: str = 'tests/clock'
_tests: Set[str] = {
    'test_time.py',
    'test_widget.py'
}
_tests_abs_path: Set[str] = set(map(lambda test: os.path.join(_tests_dir_path, test), _tests))


def main() -> None:
    """Run a test suite."""
    for test in _tests_abs_path:
        easypy.run(testscript=test)
