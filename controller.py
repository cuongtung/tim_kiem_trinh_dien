# from flask import Flask
import json
import requests
from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)
items = list(range(100))

def get_items(offset=0, per_page=10):
    return items[offset: offset + per_page]

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/search", methods=['GET'])
def search():
    inp = request.args.get('input')
    input = "title:" + inp + " OR content:" + inp
    query = quote(input)
    api = "http://localhost:8990/solr/core11/select?q=" + query +"&rows=30000"
    r = requests.get(api)
    r = json.dumps(r.json())
    result = json.loads(r)

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(items)
    pagination_users = get_items(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')


    return render_template("result.html", numFound=result['response']['numFound'], time=result['responseHeader']['QTime'],docs=result['response']['docs'], query=inp,
                           items=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)

if __name__ == "__main__":
    app.run()
