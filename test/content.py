from flask import Flask
from flask import jsonify

# from  import TicketPredict

app = Flask(__name__)
# ticket_predict = TicketPredict()

@app.route('/')
def ticket():
    # pre_dict = ticket_predict.run()
    # return jsonify(pre_dict)
    pass


def add_urls(blue):

    post_urls = {
        # '/ticket_list': activity.list_id_name,

    }

    for url in post_urls:
        blue.add_url_rule(url, url.replace('/', '_'), post_urls[url], methods=('OPTIONS', 'POST'))

if __name__ == '__main__':
    app.run()
