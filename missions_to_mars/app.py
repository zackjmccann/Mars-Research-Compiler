from flask import Flask, jsonify, render_template
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
from scrape_mars import scrape
import pymongo

app = Flask(__name__)

# conn = 'mongodb://localhost:27017'

# client = pymongo.MongoClient(conn)

# db = client.mars_data

# db.mars.insert_many([scrape()])

@app.route("/")
def index():
    return(render_template('index.html'))
    
# call and invoke the function
@app.route("/scrape")
def webScrape():
    mars_scrape = scrape()
    return(render_template('scrape.html', mars_scrape=mars_scrape))

if __name__ == "__main__":
    app.run(debug=True)