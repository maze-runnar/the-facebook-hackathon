import os, sys
from wit import Wit
from gnewsclient import gnewsclient

access_token = "HC3C2BPRJMZHDB6L3PEJR2OMGTCM2RTQ"
 
client = Wit(access_token = access_token)

# available news categories
news_categories = [('sports', 'sports news'), ('political', 'political news'), ('business', 'business news'), 
				   ('top stories', 'top stories news'), ('world', 'world news'), ('national', 'national news'), 
					('technology', 'technology news'), ('entertainment', 'entertainment news')]

# a help message
HELP_MSG = """
Hey! I am NewsBot. 
I can provide you news from all around the world in different languages, on different topics! 
Try any of these categories. :)
"""


def wit_response(message_text):
    resp = client.message(message_text)
    # entity = None
    # value = None
    # try:
    #     entity = list(resp['entities'])[0]
    #     value = resp['entities'][entity][0]['value']
    # except:
    #     pass
    # return (entity,value)
    categories = {'newstype':None, 'location':None}
    
    entities = list(resp['entities'])
    for entity in entities:
        categories[entity] = resp['entities'][entity][0]['value']
    
    return categories

def get_news_elements(categories):
    news_client = gnewsclient()
    news_client.query = ''

    if categories['newstype'] != None:
        news_client.query += categories['newstype'] + ' '

    if categories['location'] != None:
        news_client.query += categories['location'] 

    news_items = news_client.get_news()

    elements = []

    for item in news_items:
        element = {
                    'title' : item['title'],
                    'buttons' : [{
                                'type': 'web_url',
                                'title': "Read more",
                                'url': item['link']
                    }],
                    'image_url': item['img']
        }
        elements.append(element)

    return elements   
#print(get_news_elements(wit_response('I want sport news from india')))