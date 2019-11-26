from flask import Flask, jsonify
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
from scrape_mars import scrape


app = Flask(__name__)


@app.route("/")
def welcome():
    return(
        f"Welcome Page"
    )

# call and invoke the function
@app.route("/scrape")
def webScrape():
    return (scrape())

if __name__ == "__main__":
    app.run(debug=True)