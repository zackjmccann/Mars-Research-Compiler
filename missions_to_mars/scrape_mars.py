import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image = soup.footer.a['data-fancybox-href']

x = 'https://www.jpl.nasa.gov'
featured_image_url = x + image

tweet = 'https://twitter.com/marswxreport?lang=en'

response = requests.get(tweet)
soup = BeautifulSoup(response.text, 'lxml')

results = soup.body.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text

facts = 'https://space-facts.com/mars/'

table = pd.read_html(facts)
mars_facts = table[0].to_html()

facts_table = mars_facts.replace('\n', '')

hemi_links = []
hemi_titles = []
hemis = ['valles_marineris','cerberus','schiaparelli','syrtis_major']
hemi_url = [f'https://astrogeology.usgs.gov/search/map/Mars/Viking/{x}_enhanced' for x in hemis]

for x in hemi_url:
    hemi_response = requests.get(x)
    soup = BeautifulSoup(hemi_response.text, 'lxml')
    hemi_links.append(soup.body.ul.find_all('li')[0].a['href'])
    hemi_titles.append(soup.head.title.text.split('Enhanced')[0])

hemi_dicts = [
    {"title": hemi_titles[0], 'img_url': hemi_links[0]},
    {"title": hemi_titles[1], 'img_url': hemi_links[1]},
    {"title": hemi_titles[2], 'img_url': hemi_links[2]},
    {"title": hemi_titles[3], 'img_url': hemi_links[3]},
]