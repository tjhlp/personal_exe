from flask import Flask
from flask import jsonify

from test_excrise.dual_colored_ball.ticket import TicketPredict

app = Flask(__name__)
ticket_predict = TicketPredict()



def add_urls(blue):

    post_urls = {
        '/ticket_list': ticket_predict.run(),

    }

    for url in post_urls:
        blue.add_url_rule(url, url.replace('/', '_'), post_urls[url], methods=('OPTIONS', 'POST'))


if __name__ == '__main__':
    app.run()
