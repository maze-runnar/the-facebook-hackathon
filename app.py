import os
import sys
import json
from wit import Wit
import webbrowser
import requests
from flask import Flask, request

from pymessenger.bot import Bot

from bs4 import BeautifulSoup



app = Flask(__name__)       # Initializing our Flask application
ACCESS_TOKEN = "EAAIUGcZC0tmABAI51LvwbZCUNtqOX0Dq0krU6gqk5QxgClHJ0aZBdZCfEwaGslOFeaNjoSy7jbXCMp59xgEhapjE0jCC31HOdsVcZAlsSkZBsHcI4zf3jAujZBx1Nj4sJVOeeqZAccQmMVH9yqG1Ji2ZAGG1lBU08uvFkG6MBTzF03AZDZD"
VERIFY_TOKEN = "themazerunner"
counts = 0
bot = Bot(ACCESS_TOKEN)

client = Wit("HC3C2BPRJMZHDB6L3PEJR2OMGTCM2RTQ")

def process(msg):
    hope =  client.message(msg)
    intent_name = hope["intents"][0]["name"]
    val = ""
    if intent_name == "Greetings":
        print("hello from the otherside!")
    elif intent_name == "Article_Name":
        val = hope["entities"]['article_name:article_name'][0]['value']
        #webbrowser.open("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + val)
    elif intent_name == "Author_Name":
        val = hope["entities"]['author_name:author_name'][0]['value']
        #webbrowser.open("https://scholar.google.com/citations?view_op=search_authors&mauthors="+ val +"&hl=en&oi=ao")
    print(val)
    return str(val)


def scrap(user_name):
    url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + str(user_name)
    source_code = requst.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    ans  = []
    for link in soup.find_all("a"):
        ans.append(link.string)
    return ans[0]


# Importing standard route and two requst types: GET and POST.
# We will receive messages that Facebook sends our bot at this endpoint
# method to reply to a message from the sender
def reply_quick(user_id, msg):
    data = {
          "recipient":{
            "id":user_id
          },
          "messaging_type": "RESPONSE",
          "message":{
            "text": "For what you are searching for..",
            "quick_replies":[
              {
                "content_type":"text",
                "title":"Author",
                "payload":"Author",
                "image_url":"https://live.mrf.io/statics/i/ps/www.herald.co.zw/wp-content/uploads/sites/2/2018/07/Author-680-x-300-1.jpg?width=1200&enable=upscale"
              },{
                "content_type":"text",
                "title":"Book",
                "payload":"Book",
                "image_url":"https://www.theguardian.pe.ca/media/photologue/photos/cache/360_large.jpg"
              },{
                "content_type":"text",
                "title":"Article",
                "payload":"Article",
                "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Purple.svg/1200px-Purple.svg.png"
              },
              {
                "content_type":"text",
                "title":"Quit",
                "payload":"Quit",
                "image_url":"https://content.linkedin.com/content/dam/business/talent-solutions/global/en_us/blog/2015/03/quit-job.jpg"
              }
            ]
          }
        }
            
    # Post request using the Facebook Graph API v2.6
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def generic_reply_author(user_id, msg):
    data = {
        "recipient":{
        "id":user_id
      },
      "message":{
        "attachment":{
          "type":"template",
          "payload":{
            "template_type":"generic",
            "elements":[
                {
                "title":"Open Library",
                "image_url":"https://repository-images.githubusercontent.com/69609/6d346300-3bc4-11ea-81da-6ff573cc4987",
                "subtitle":"Open Library is an open, editable library catalog, building towards a web page for every book ever published. Read, borrow, and discover more than 3M books ...",
                "default_action": {
                  "type": "web_url",
                  "url": "https://openlibrary.org/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://openlibrary.org/",
                    "title":"Visit Website"
                  },{
                    "type":"web_url",
                    "url":"https://openlibrary.org/search/authors?q=" + msg.replace(" ", "%20") + "&has_fulltext=true",
                    "title":"View Result"
                  }              
                ]      
              },
               {
                "title":"Google Scholar",
                "image_url":"https://www.clipartkey.com/mpngs/m/124-1242841_logo-google-scholar-icon.png",
                "subtitle":"Google Scholar library is your personal collection of articles. You can save articles right off the search page, organize them by topic, and use the power of Scholar",
                "default_action": {
                  "type": "web_url",
                  "url": "https://scholar.google.com/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://scholar.google.com/",
                    "title":"Visit Website"
                  },{
                    "type":"web_url",
                    "url":"https://scholar.google.com/citations?view_op=search_authors&mauthors=" + msg.replace(" ", "%20"),
                    "title":"View Result"
                  }              
                ]      
              }
            ]
          }
        }
      }

    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


def generic_reply(user_id, msg):
    data = {
        "recipient":{
        "id":user_id
      },
      "message":{
        "attachment":{
          "type":"template",
          "payload":{
            "template_type":"generic",
            "elements":[
                {
                "title":"Open Library",
                "image_url":"https://repository-images.githubusercontent.com/69609/6d346300-3bc4-11ea-81da-6ff573cc4987",
                "subtitle":"Open Library is an open, editable library catalog, building towards a web page for every book ever published. Read, borrow, and discover more than 3M books ...",
                "default_action": {
                  "type": "web_url",
                  "url": "https://openlibrary.org/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://openlibrary.org/",
                    "title":"Visit Website"
                  },{
                    "type":"web_url",
                    "url":"https://openlibrary.org/search?q=" + msg.replace(" ", "%20") + "&mode=ebooks&has_fulltext=true",
                    "title":"View Result"
                  }              
                ]      
              },
               {
                "title":"Google Scholar",
                "image_url":"https://www.clipartkey.com/mpngs/m/124-1242841_logo-google-scholar-icon.png",
                "subtitle":"Google Scholar library is your personal collection of articles. You can save articles right off the search page, organize them by topic, and use the power of Scholar",
                "default_action": {
                  "type": "web_url",
                  "url": "https://scholar.google.com/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://scholar.google.com/",
                    "title":"Visit Website"
                  },{
                    "type":"web_url",
                    "url":"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + msg.replace(" ", "%20"),
                    "title":"View Result"
                  }              
                ]      
              },
              {
                "title":"Academic",
                "image_url":"https://www.stjegypt.com/uploads/267718018507.jpg",
                "subtitle":"Search ResultsWeb resultsMicrosoft Academic: Homeacademic.microsoft.com This website is powered by Microsoft Academic Graph (MAG) data and Microsoft Academic Knowledge Exploration Service (MAKES) hosted API's. ",
                "default_action": {
                  "type": "web_url",
                  "url": "https://academic.microsoft.com/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://academic.microsoft.com",
                    "title":"View Website"
                  },{
                    "type":"web_url",
                    "url":"https://academic.microsoft.com/search?q=" + msg.replace(" ", "%20"),
                    "title":"View Result"
                  }              
                ]      
              },
              {
                "title":"Google Books",
                "image_url":"https://purepng.com/public/uploads/large/purepng.com-play-books-icon-android-lollipopsymbolsiconsgooglegoogle-iconsandroid-lollipoplollipop-iconsandroid-50-7215225972313gef0.png",
                "subtitle":"Google Books is a service from Google Inc. that searches the full text of books and magazines that Google has scanned, converted to text using optical character recognition, and stored in its digital database",
                "default_action": {
                  "type": "web_url",
                  "url": "https://www.google.com/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"View Website"
                  },{
                    "type":"web_url",
                    "url":"https://www.google.com/search?tbm=bks&q="+ msg.replace(" ", "%20"),
                    "title":"View Result"
                  }              
                ]      
              },
              {
                "title":"Core",
                "image_url":"https://assets.entrepreneur.com/content/3x2/2000/20191219170611-GettyImages-1152794789.jpeg",
                "subtitle":"Increasing the visibility of content in repositories and journals. Tools and global scholarly analytics for institutions, funders and policy makers.",
                "default_action": {
                  "type": "web_url",
                  "url": "https://core.ac.uk/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://core.ac.uk/",
                    "title":"View Website"
                  },{
                    "type":"web_url",
                    "url":"https://core.ac.uk/" + msg.replace(" ", "%20"),
                    "title":"View Result"
                  }              
                ]      
              },
              {
                "title":"Semantic Scholar",
                "image_url":"https://techcrunch.com/wp-content/uploads/2016/11/s2.png?w=730&crop=1",
                "subtitle":"Semantic Scholar uses groundbreaking AI and engineering to understand the semantics of scientific literature to help Scholars discover relevant research.",
                "default_action": {
                  "type": "web_url",
                  "url": "https://www.semanticscholar.org/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://www.semanticscholar.org/",
                    "title":"View Website"
                  },{
                    "type":"web_url",
                    "url":"https://www.semanticscholar.org/search?q=" + msg.replace(" ", "%20") +"&sort=relevance",
                    "title":"View Result"
                  }              
                ]      
              },
              {
                "title":"SciElo",
                "image_url":"https://hgsa.co.za/wp-content/uploads/2019/09/logo_scielo-1.jpg",
                "subtitle":"SciELO is a bibliographic database, digital library, and cooperative electronic publishing model of open access journals.",
                "default_action": {
                  "type": "web_url",
                  "url": "https://search.scielo.org/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://search.scielo.org/",
                    "title":"Visit Website"
                  },{
                    "type":"web_url",
                    "url":"https://search.scielo.org/?lang=en&q=" + msg.replace(" ", "%20"),
                    "title":"View Result"
                  }              
                ]      
              },
              {
                "title":"Dimensions",
                "image_url":"https://www.dimensions.ai/wp-content/uploads/2019/07/social-media-card.png",
                "subtitle":"The Next Evolution in Linked Scholarly Information. Dimensions is the most comprehensive research grants database which links grants to millions of resulting publications, clinical trials and patents",
                "default_action": {
                  "type": "web_url",
                  "url": "https://app.dimensions.ai/",
                  "webview_height_ratio": "compact",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://app.dimensions.ai/",
                    "title":"Visit Website"
                  },{
                    "type":"web_url",
                    "url":"https://app.dimensions.ai/discover/publication?search_text=" + msg.replace(" ", "%20"),
                    "title":"View Result"
                  }              
                ]      
              }
            ]
          }
        }
      }

    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)



def reply(user_id, msg):
    data = {
        "recipient":{
            "id":user_id
          },
        "messaging_type": "RESPONSE",
        "message":{
            "text":msg
        }
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

# GET request to handle the verification of tokens
@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

# POST request to handle in coming messages then call reply()
@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events
    previous_message = ""
    data = request.get_json()
    
    #log(data)  # you may not want to log every incoming message in production, but it's good for testing
    #reply("sender_id", "Welcome to a smart helpful bot To help in your Academic works")
    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text
                    #message_text = "hi"
                    ##send_message(sender_id, "roger that!")
                    
                    if(message_text == "hi" or message_text == "hello"):
                        reply_quick(sender_id, message_text)
                    

                    elif(message_text == "Book"):
                        
                        reply(sender_id, "Enter the book name like book: shawshank redemption")
                        
                    elif(message_text == "Author"):
                
                        reply(sender_id, "Enter the author name like author: stephen king")
                        
                    elif(message_text == "Article"):
                        
                        reply(sender_id, "Enter the article name like article: harry potter")
    

                    elif(message_text == "Quit"):
                        reply(sender_id, "see you later with another research")
                        
                    else:
                        # reply(sender_id, "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + message_text.replace(" ", "%20"))
                        # reply(sender_id, "https://academic.microsoft.com/search?q=" + message_text)
                        # reply(sender_id, "https://www.google.com/search?tbm=bks&q="+message_text)
                        # reply(sender_id, "https://core.ac.uk/search?q=" + message_text)
                        # reply(sender_id, "https://www.semanticscholar.org/search?q=" + message_text +"&sort=relevance")
                        if("article" in message_text.lower()):
                            message_text = message_text.replace("article:", "")
                            generic_reply(sender_id, message_text)
                            reply_quick(sender_id, message_text)
                        elif("author" in message_text.lower()):
                            message_text = message_text.replace("author:", "")
                            generic_reply_author(sender_id, message_text)
                            reply_quick(sender_id, message_text)
                        elif("book" in message_text.lower()):
                            message_text = message_text.replace("book:", "")
                            generic_reply(sender_id, message_text)
                            reply_quick(sender_id, message_text)
                    
    return "ok"

# Run the application.
if __name__ == '__main__':
    app.run(debug=True)