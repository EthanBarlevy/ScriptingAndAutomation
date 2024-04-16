import PySimpleGUI as sg
import requests
import urllib.request
from bs4 import BeautifulSoup

sap = 0

def getLinks(sap):
    links = []
    for image in sap.find_all('img'):
        link = image.get('src')
        if "static-assets" in link:
            links.append(link)
    return links

def buttonClicked(slap, extended):
    r = requests.get('https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/?cardName=&cardText=&evolvesFrom=&card-grass=on&simpleSubmit=&format=unlimited&hitPointsMin=0&hitPointsMax=340&retreatCostMin=0&retreatCostMax=5&totalAttackCostMin=0&totalAttackCostMax=5&particularArtist=')
    slap = (BeautifulSoup(r.text, features='html.parser'))
    links = getLinks(slap)
    row = 1
    if len(links) == 0:
        print("too many requests")
    for link in links:
        save_name = f'image{row}.png'
        urllib.request.urlretrieve(link, save_name)
        extended.append([sg.Image(save_name)])
        row += 1

layout = [[sg.Button('Scrape', key='SCRAPE')]]

window = sg.Window('Pokemon Scraper', layout)

extended = []

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "SCRAPE":
        buttonClicked(sap, extended)
        window.extend_layout(window, extended)


