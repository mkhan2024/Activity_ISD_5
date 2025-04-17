"""Module for managing a sports league with teams."""

__author__ = "Md Apurba Khan"
__version__ = "1.6.0"
__credits__ = "ACE Faculty"

from team.team import Team

class League:
    """
    Manages a collection of teams in a sports league.
    """
    def __init__(self, name: str):
        """
        Initialize a League instance with a name.
        
        Parameters:
            name (str): The name of the league.
        
        Raises:
            ValueError: If name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self.__name = name
        self.__teams = []

    def __str__(self) -> str:
        """
        Return a string representation of the league.
        
        Returns:
            str: Details of the league and its teams.
        """
        team_details = ', '.join(str(team) for team in self.__teams)
        return f"League: {self.__name}, Teams: [{team_details}]"

    def add_team(self, team: Team) -> None:
        """
        Add a team to the league.
        
        Parameters:
            team (Team): The team to add.
        
        Raises:
            ValueError: If team is not a Team instance.
        """
        if not isinstance(team, Team):
            raise ValueError("team must be a Team instance")
        self.__teams.append(team)

    @property
    def name(self) -> str:
        """
        Get the name of the league.
        
        Returns:
            str: The league's name.
        """
        return self.__name

    @property
    def teams(self) -> list:
        """
        Get the list of teams in the league.
        
        Returns:
            list: List of Team objects.
        """
        return self.__teams