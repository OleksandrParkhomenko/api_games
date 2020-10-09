import requests
import json


class API:

    def __init__(self, developer_name="oleksandr_parkhomenko"):
        self.developer_name = developer_name
        self.URL = "https://www.magetic.com/c/test?api=1&amp;name={}".format(developer_name)
        self.games = {}
        self.json_games = None

    def add_games(self, games):
        # check if there any new game to be added
        new_game_appear = False
        for game in games:
            try:
                self.games[game] += 1
            except KeyError:
                self.games[game] = 1
                new_game_appear = True
        return new_game_appear

    def get_names_game(self):
        no_new_games_counter = 0  # count request without any new game in a raw
        request_conter = 0
        MAX_REPEATS_IN_A_ROW = 50  # should be proved by math or smth, but got the value from number of test :)
        while no_new_games_counter < MAX_REPEATS_IN_A_ROW:
            resp = requests.get(self.URL)
            if resp.ok:
                # skip responses with ERROR
                if resp.status_code == 501 or resp.text.find("Error") != -1:
                    continue

                # read the names of the games in current response, count their occurrence
                new_games = resp.text.split(";")
                new_games = filter(None, new_games)
                new_games_appear = self.add_games(new_games)

                # count times of response with all duplicating games
                if not new_games_appear:
                    no_new_games_counter += 1
                else:
                    no_new_games_counter = 0
                request_conter += 1

        if __name__ == "__main__":
            print("It takes {} requests. \nYour API have {} games".format(request_conter, len(self.games)))

    def build_json(self):
        # reformat existing data to json
        list_games = []
        for game_name in self.games:
            list_games.append({
                "gamename": game_name,
                "number": self.games[game_name]
            })
        self.json_games = json.dumps(list_games)

    def print_json(self):
        print(self.json_games)


if __name__ == "__main__":
    api = API()
    api.get_names_game()
    api.build_json()
    api.print_json()
