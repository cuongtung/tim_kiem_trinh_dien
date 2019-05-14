# from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/search", methods=['GET'])
def search():
	user = request.args.get('input')
  	return redirect(url_for('result',input = user))

@app.route("/result/<input>")
def result(input):
  return render_template("result.html", input=input)

if __name__ == "__main__":
  app.run()