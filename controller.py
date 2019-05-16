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
    api = "http://localhost:8990/solr/mycore/select?q=" + query
    r = requests.get(api)
    # result = r.json()
    r = json.dumps(r.json())
    result = json.loads(r)
    # return render_template("result.html",result=result['response']['numFound'])
    return render_template("result.html", numFound=result['response']['numFound'], time=result['responseHeader']['QTime'],docs=result['response']['docs'])

if __name__ == "__main__":
    app.run()
