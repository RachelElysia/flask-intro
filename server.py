"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
    Hi! This is the home page.
    <p><a href="/hello">Say Hello!</a></p>
    <p><a href="/diss">Get Dissed!</a></p>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
            <select name="compliment">
              <option value="awesome">awesome</option>
              <option value="terrific">terrific</option>
              <option value="fantastic">fantastic</option> 
              <option value="neato">neato</option>
              <option value="fantabulous">fantabulous</option>
              <option value="wowza">wowza</option>           
            </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def get_diss():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss-person">
          What's your name? <input type="text" name="person">
            <select name="dissdished">
              <option value="stupid">stupid</option>
              <option value="average">average</option>
              <option value="annoying">annoying</option> 
              <option value="dim">dim</option>
              <option value="moody">moody</option>
              <option value="ass-backwards">ass-backwards</option>           
            </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss-person')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    dissdished = request.args.get("dissdished")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss to You</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, dissdished)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
