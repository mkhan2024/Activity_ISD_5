"""Client program to launch the sports league GUI application."""

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

from sports_app.sports_app import SportsApp
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    """Launch the SportsApp GUI application."""
    app = QApplication(sys.argv)
    window = SportsApp()
    window.show()
    sys.exit(app.exec())