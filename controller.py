# from flask import Flask
import requests
from urllib.parse import quote

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def main():

	return render_template("index.html")

@app.route("/search", methods=['GET'])
def search():
    input = request.args.get('input')
    input = quote(input)
    api = "http://localhost:8983/solr/it4853-1/select?q=title"+input
    r = requests.get(api)
    r = r.json()
    for e in r:
        e{'title'}
        e{'content'}
    print(r.json)

    return redirect(url_for('result', input = r.json)

@app.route("/result/<input>")
def result(input):
  return render_template("result.html", input=input)

if __name__ == "__main__":
  app.run()