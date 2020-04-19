from flask import Flask
import cmd

args = cmd.parse()

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
