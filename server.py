from flask import Flask, request
from api_games import API
import json

app = Flask(__name__)
api = API()


@app.route('/')
@app.route('/test')
def test():
    """
    Return info about existing games in API in JSON format
    """
    api.get_names_game()
    api.build_json()
    return api.json_games


@app.route('/get_number')
def number():
    """
    Return the number of existing games in API
    """
    num_of_games = len(api.games)
    if num_of_games > 0:
        return "You have {} games".format(num_of_games)
    else:
        return "Your API doesn't have any game or you haven't count it.\n Go to 127.0.0.1:5000/test to do this."


@app.route('/search')
def search(game_name="", keyword=""):
    """
    Return search results
    """
    game_name = request.args.get('game_name')
    keyword = request.args.get('keyword')

    if game_name:
        try:
            return json.dumps(api.games[game_name])
        except KeyError:
            return "There is no game with such name '{}'".format(game_name)

    elif keyword:
        suitable_games = []
        for game_name in api.games:
            try:
                if game_name.find(keyword) != -1:
                    suitable_games.append({
                        "gamename": game_name,
                        "number": api.games[game_name]
                    })
            except KeyError:
                continue

        # return message about unsuccessful search or result
        if len(suitable_games) == 0:
            return "There is no game with '{}' keyword".format(keyword)
        return json.dumps(suitable_games)
    return test


if __name__ == '__main__':
    app.run()
