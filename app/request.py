import urllib.request,json
from .models import Quote
import requests
from config import Config

#Getting the quotes base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config["QOUTES_API_BASE_URL"]


def get_quotes():
    '''
    Function that gets the json response to the url request
    '''
    response=requests.get(base_url).json()
    random_quote = Quote(response.get("author"), response.get("quote"))

    return random_quote