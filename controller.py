# from flask import Flask
import requests
import json
from flask import Flask, render_template, redirect, url_for, request
from urllib.parse import quote
app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/search", methods=['GET'])
def search():
	input = request.args.get('input')
	input = "title:"+input
	query = quote(input)
	api = "http://localhost:8983/solr/it4853-1/select?q=" + input
	r = requests.get(api)
	result = r.json()
	return render_template("result.html", result=result)

# @app.route("/result/<input>")
# def result(input):
#   return render_template("result.html", input=input)

if __name__ == "__main__":
  app.run()