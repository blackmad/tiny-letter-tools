#!/usr/bin/python
from flask import Flask
import StringIO
from flaskrun import flaskrun
from tinyletter import TinyLetter

app = Flask(__name__)

@app.route('/favicon.ico')
def ico404():
  return ''

@app.route('/<name>')
def serve_rss(name):
  print name
  output = StringIO.StringIO()
  url = 'https://tinyletter.com/' + name
  tl = TinyLetter(url)
  tl.as_rss(output)
  contents = output.getvalue()
  return contents

flaskrun(app)


