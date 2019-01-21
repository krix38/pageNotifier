import json
import time
import requests
import os
from bs4 import BeautifulSoup

def pagePassesPredicate(config):
    url = config['url']
    predicate = config['predicate']
    selector = config['selector']

    request = requests.get(url)
    pageContent = request.text
    soup = BeautifulSoup(pageContent, 'html.parser')

    elements = soup.select(selector)
    return any(eval(predicate)(element) for element in elements)

with open('config.json') as configFile:
    config = json.load(configFile)

while not pagePassesPredicate(config):
    time.sleep(config['interval'])

os.system(config['executeOnSuccess'])
