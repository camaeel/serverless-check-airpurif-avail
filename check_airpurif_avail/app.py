import json
import logging
import requests
import re
import os
from bs4 import BeautifulSoup

#setup logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def lambda_handler(event, context):
    URL_PAGE1 = "https://usunsmog.pl/wypozycz-oczyszczacz/"
    URL_AVAILABILITY = "https://usunsmog.pl/api-stock/?api"

    logger.debug("NOTIFICATION_EMAIL: %s", str(os.environ['NOTIFICATION_EMAIL']))
    logger.debug("PURIFIER_MODEL_NAME: %s", str(os.environ['PURIFIER_MODEL_NAME']))
    logger.debug("Event received: %s", str(event))

    page1 = requests.get(URL_PAGE1)
    avail_api = requests.get(URL_AVAILABILITY)

    page1_content = BeautifulSoup(page1.content, 'html.parser') 
    availability_data = avail_api.json()
    logger.debug("Pages loaded")
    page1_data = parse_json_data_from_html(page1_content)
    models_data = page1_data['state']['questions']['modelsInfo']
    
    skus = get_skus(models_data, os.environ['PURIFIER_MODEL_NAME'])
    availability = check_skus_avilability(skus, availability_data)

    return {
        "statusCode": 200,
        "body": "Ok"
    }

def parse_json_data_from_html(content):
    #extract script element with data
    data_script_tag_content = content.find(id='__nuxt').next_sibling.contents[0]
    device_data = data_script_tag_content[data_script_tag_content.index('=')+1:]

    #do the regexp substition magic
    fixed_quotes = re.sub(r'([{,])([a-zA-Z0-9_]+):',r'\1"\2":',device_data)
    fixed_quotes = re.sub(r':(![0-9]|null)([,}])',r':"\1"\2',fixed_quotes)
    
    return json.loads(fixed_quotes)

def get_skus(models_data, model_name):
    return [m['sku'] for m in models_data if m['name'] == model_name]


def check_skus_avilability(skus, availability_data):
    available = []
    for sku in skus:
        for i in range(len(availability_data['material'])):
            if availability_data['material'][i] == sku and availability_data['unrestr'][i] > 0:
                available.append(sku)
                

    return available
