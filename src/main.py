from flask import Flask
import cmd
import api

args = cmd.parse()

app = Flask(__name__)
app.register_blueprint(api.api)

if __name__ == '__main__':
    app.run()
