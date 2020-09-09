from bs4 import BeautifulSoup
import urllib
import requests

# This doesn't require a token vv
def searchFromLink(link):
    if 'genius.com' in link:
        geniuspage = requests.get(link)
        html = BeautifulSoup(geniuspage.text, "html.parser")
        lyrics = html.find("div", class_="lyrics").get_text()
        return lyrics.replace(r'\n', '\n')
    else:
        return "Not a valid url!"