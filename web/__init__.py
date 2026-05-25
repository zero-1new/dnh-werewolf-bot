from threading import Thread
import os

from flask import Flask, render_template
from waitress import serve

# ============ Flask functions ============
# Init a web application, can be used to keep your bot alive with uptime services

appFlask = Flask(__name__)


@appFlask.route('/')
def home():
    return render_template('index.html')


def run():
    port = int(os.getenv("PORT", "10000"))
    serve(appFlask, host="0.0.0.0", port=port)


def keep_alive():
    thread = Thread(target=run)
    print('Start Flask separated from the bot')
    thread.start()
