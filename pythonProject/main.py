from flask import Flask, render_template

from utils.Game import Game

application = Flask(__name__)
@application.route('/init')
def test():
    game_1st = Game('Tetris', 'Puzzle', 'Atari')
    game_2nd = Game('God of War', 'Rack n Slack', 'Play Station 2')
    games_list = [game_1st, game_2nd]
    return render_template('list.html', tittle='Games', games=games_list)
application.run()