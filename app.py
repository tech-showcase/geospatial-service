from flask import Flask
from src import cmd
from src import api

args = cmd.parse()

app = Flask(__name__)
app.register_blueprint(api.api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port)
