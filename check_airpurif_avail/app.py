import json
import logging
import requests

from bs4 import BeautifulSoup

#setup logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def lambda_handler(event, context):
    URL_PAGE1 = "https://usunsmog.pl/wypozycz-oczyszczacz/"
    URL_AVAILABILITY = "https://usunsmog.pl/api-stock/?api"

    # logger.debug("Env: %s", str(os.environ))
    logger.debug("Event: %s", str(event))

    page1 = requests.get(URL_PAGE1)
    avail_api = requests.get(URL_AVAILABILITY)

    page1_data = BeautifulSoup(page1.content, 'html.parser') 
    avail_data = avail_api.json()
    logger.debug("Pages loaded")

    data_script_tag_content = page1_data.find(id='__nuxt').next_sibling.contents[0]
    device_data = data_script_tag_content[data_script_tag_content.index('=')+1:]
    json.load(device_data)
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": "Ok"
    }
