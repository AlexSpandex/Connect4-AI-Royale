"""this is the leaderboard data file"""

import json
import os


class LeaderboardData:
    """Sets up the leader board data"""

    def __init__(self, filename="leaderboard.json"):
        """
        Initialize the LeaderboardData instance.

        Parameters:
        - filename (str): The name of the JSON file storing the leaderboard data.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(script_dir, filename)
        self.load_leaderboard()

    def update_leaderboard(self, player1, player2):
        """
        Update the leaderboard with the results of a game between two players.

        Parameters:
        - player1 (str): The name of the first player.
        - player2 (str): The name of the second player.
        """
        if player1 not in self.data:
            self.data[player1] = {"wins": 0, "losses": 0}

        if player2 not in self.data:
            self.data[player2] = {"wins": 0, "losses": 0}

        self.data[player1]["wins"] += 1
        self.data[player2]["losses"] += 1

    def save_leaderboard(self):
        """
        Save the current leaderboard data to the specified JSON file.
        """
        try:
            with open(self.filename, "w") as file:
                json.dump(self.data, file)
            print("Leaderboard saved successfully")
        except Exception as e:
            print(f"Error saving leaderboard: {e}")

    def load_leaderboard(self):
        """
        Load the leaderboard data from the specified JSON file.

        If the file does not exist, create an empty leaderboard.
        """
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            # Create an empty leaderboard if the file doesn't exist
            self.data = {}
        except Exception as e:
            print(f"Error loading leaderboard: {e}")

    def display_leaderboard(self):
        """
        Display the current leaderboard data in the console.
        """
        print("Leaderboard:")
        for player, stats in self.data.items():
            print(f"{player}: Wins - {stats['wins']}, Losses - {stats['losses']}")
