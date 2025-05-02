
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    current_time = datetime.now()
    return '{' + '"time": "' + current_time.strftime("%H:%M:%S") + '"}', 200

if __name__ == '__main__':
    app.run()

