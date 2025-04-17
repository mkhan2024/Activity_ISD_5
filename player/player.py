"""Module for managing a player in a sports team."""

__author__ = "Md Apurba Khan"
__version__ = "1.3.0"
__credits__ = "ACE Faculty"

class Player:
    """Represents a player in a sports team."""

    def __init__(self, name: str, age: int, position: str):
        """Initialize a Player instance with name, age, and position.

        Args:
            name (str): The player's name.
            age (int): The player's age.
            position (str): The player's position on the team.

        Raises:
            ValueError: If name or position is not a string, or age is not an integer.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if not isinstance(position, str):
            raise ValueError("Position must be a string")
        self.__name = name
        self.__age = age
        self.__position = position

    @property
    def name(self) -> str:
        """Get the player's name.

        Returns:
            str: The player's name.
        """
        return self.__name

    @property
    def age(self) -> int:
        """Get the player's age.

        Returns:
            int: The player's age.
        """
        return self.__age

    @property
    def position(self) -> str:
        """Get the player's position.

        Returns:
            str: The player's position.
        """
        return self.__position

    def __str__(self) -> str:
        """Return a string representation of the player.

        Returns:
            str: Details of the player.
        """
        return f"Name: {self.__name}, Age: {self.__age}, Position: {self.__position}"