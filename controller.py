# from flask import Flask
import json
import requests
from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/search", methods=['GET'])
def search():
    input = request.args.get('input')
    input = "title:" + input
    query = quote(input)
    api = "http://localhost:8983/solr/it4853-1/select?q=" + query
    r = requests.get(api)
    result = r.json()
    # result = json.loads(result)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run()
