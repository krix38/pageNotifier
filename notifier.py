import json
import time
import requests
from bs4 import BeautifulSoup

def checkRequest(config):
    uri = config['uri']
    predicate = config['predicate']
    selector = config['selector']

    request = requests.get(uri)
    pageContent = request.text
    soup = BeautifulSoup(pageContent, 'html.parser')

    element = soup.select(selector)
    predicatePass = len(list(filter(eval(predicate), element))) > 0
    print(predicatePass) #TODO: run some script defined in config

with open('config.json') as configFile:
    config = json.load(configFile)

while True:
    checkRequest(config)
    time.sleep(config['interval'])
