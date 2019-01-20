import json
import time
import requests
import os
from bs4 import BeautifulSoup

def pagePassesPredicate(config):
    uri = config['uri']
    predicate = config['predicate']
    selector = config['selector']

    request = requests.get(uri)
    pageContent = request.text
    soup = BeautifulSoup(pageContent, 'html.parser')

    elements = soup.select(selector)
    return any(eval(predicate)(element) for element in elements)

with open('config.json') as configFile:
    config = json.load(configFile)

while not pagePassesPredicate(config):
    time.sleep(config['interval'])

os.system(config['executeOnSuccess'])