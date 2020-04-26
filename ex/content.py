from flask import Flask
from flask import jsonify

from ex.ticket import TicketPredict

app = Flask(__name__)
ticket_predict = TicketPredict()

@app.route('/')
def ticket():
    pre_dict = ticket_predict.run()
    return jsonify(pre_dict)


if __name__ == '__main__':
    app.run()
