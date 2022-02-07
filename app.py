from turtle import title
from flask import Flask, render_template, request

app = Flask(__name__)

class Games():
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console
     
gameOne = Games('Horizon Zero Down', 'Action', 'Playstation')
gameTwo = Games('Uncharted', 'Action', 'Playstation')
gameThree = Games('GTA5', 'Action', 'Playstaion')
gameFour = Games('ZLA', 'Action', 'Playstaion')

listGames = [gameOne, gameTwo, gameThree, gameFour]

@app.route('/', methods=['POST', 'GET'])
def index():
    tittlePage = 'Home | GamesBy'
    tittleH1 = 'Games'
    return render_template('index.html', title=tittlePage, titleh1=tittleH1, games=listGames)

@app.route('/new-game')
def newgame():
    titlePage = 'New game | GamesBy'
    titleH1 = 'Register new game'
    return render_template('newgame.html', title=titlePage, titleh1=titleH1)

@app.route('/create-game', methods=['POST',])
def createGame():
    titlePage = 'Create game | GamesBy' 
    name = request.form['name_name']
    category = request.form['category_name']
    console = request.form['console_name']

    game = Games(name, category, console)

    listGames.append(game)

    return render_template('index.html', title=titlePage, games=listGames)