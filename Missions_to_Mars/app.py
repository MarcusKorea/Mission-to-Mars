from flask import Flask,render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017")

@app.route("/")
def index():
    mars_info = mongo.db.collection.find_one()

    # Return data
    return render_template("index.html", mars=mars_info)

@app.route("/scrape")
def data_scrape():

    mars = mongo.db.mars

    data = scrape_mars.scrape_all()
    mars.update({}, data, upsert=True)
    return "Scraping done!"

# main
if __name__ == "__main__":
    app.run()
    app.debug = True