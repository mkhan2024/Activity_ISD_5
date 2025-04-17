"""Module for managing a team in a sports league."""

__author__ = "Md Apurba Khan"
__version__ = "1.5.0"
__credits__ = "ACE Faculty"

from player.player import Player

class Team:
    """Represents a team in a sports league."""

    def __init__(self, name: str, city: str):
        """Initialize a Team instance with name and city.

        Args:
            name (str): The team's name.
            city (str): The city where the team is based.

        Raises:
            ValueError: If name or city is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(city, str):
            raise ValueError("City must be a string")
        self.__name = name
        self.__city = city
        self.__players = []

    @property
    def name(self) -> str:
        """Get the team's name.

        Returns:
            str: The team's name.
        """
        return self.__name

    @property
    def city(self) -> str:
        """Get the team's city.

        Returns:
            str: The team's city.
        """
        return self.__city

    @property
    def players(self) -> list:
        """Get the list of players on the team.

        Returns:
            list: List of Player objects.
        """
        return self.__players

    def add_player(self, player: Player) -> None:
        """Add a player to the team.

        Args:
            player (Player): The player to add.

        Raises:
            ValueError: If player is not a Player instance.
        """
        if not isinstance(player, Player):
            raise ValueError("player must be an instance of Player")
        self.__players.append(player)

    def __str__(self) -> str:
        """Return a string representation of the team.

        Returns:
            str: Details of the team and its players.
        """
        player_details = ', '.join(str(player) for player in self.__players)
        return f"Team: {self.__name}, City: {self.__city}, Players: [{player_details}]"