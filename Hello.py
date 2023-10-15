import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    f = open('mydata.json')
    players = json.load(f)
    # for i in range(len(players)):
    #     for j in range(i, len(players)):
    #         if players[i]['score'] > players[j]['score']:
    #             temp = players[i]
    #             players[i] = players[j]
    #             players[j] = temp

    return render_template('index.html', players=players)


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
