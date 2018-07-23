#import click
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello world for all our people"

if __name__ == "__main__":
	app.run()