"""Module for the main GUI application of the sports league."""

__author__ = "Md Apurba Khan"
__version__ = "1.6.0"
__credits__ = "ACE Faculty"

import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
from player.player import Player

class SportsApp(QWidget):
    """
    Main window for the sports league application.
    """
    def __init__(self):
        """
        Initialize the SportsApp main window.
        
        Parameters:
            None
        
        Returns:
            None
        """
        super().__init__()
        self.__initialize_widgets()
        self.button.clicked.connect(self.__show_message)

    def __initialize_widgets(self):
        """
        Set up the widgets for the main window.
        
        Parameters:
            None
        
        Returns:
            None
        """
        self.setWindowTitle("Sports League")
        layout = QVBoxLayout()

        # Create the table
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Position"])

        # Hard-coded data
        players = [
            Player("John Doe", 25, "Forward"),
            Player("Jane Smith", 28, "Midfielder"),
            Player("Jim Brown", 22, "Defender")
        ]

        for i, player in enumerate(players):
            self.table.setItem(i, 0, QTableWidgetItem(player.name))
            self.table.setItem(i, 1, QTableWidgetItem(str(player.age)))
            self.table.setItem(i, 2, QTableWidgetItem(player.position))

        self.table.resizeColumnsToContents()
        layout.addWidget(self.table)

        # Create the button
        self.button = QPushButton("Show Message")
        layout.addWidget(self.button)

        self.setLayout(layout)

    def __show_message(self):
        """
        Display a welcome message to the user.
        
        Parameters:
            None
        
        Returns:
            None
        """
        QMessageBox.information(self, "Welcome", "Welcome to the Team!")