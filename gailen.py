from js import console, fetch
import sqlite3 as sql
from datetime import datetime

### REFERENCE VIDEO https://www.youtube.com/watch?v=7meW2djIUYk&t=4s

### TODO - BUILD CONTACT FORM AND BLOG USING PYSCRIPT

#introduce tags to python
    #variable = Element('tag-id')
namein = Element('name')
emailin = Element('email')
phonein = Element('phone')
messagein = Element('message')
button = Element('submit')
    #<div class="pydiv">
div = Element('pydiv')

def getthethings(*args):
    #console.log('button was clicked')
    timestamp = datetime.timestamp(datetime.now())
    nameout = namein.element.value
    emailout = emailin.element.value
    phoneout = phonein.element.value
    messageout = messagein.element.value
    confirmation = create("div", classes='output text-center alert alert-info fade show')
    confirmation.element.innerText = 'Your message has been sent.'
    div.element.appendChild(confirmation.element)

    userinfo = create("div", classes='output text-center alert alert-primary fade show')
    userinfo.element.innerText = nameout + '\n' + emailout + '\n' + phoneout
    div.element.appendChild(userinfo.element)

    messageinfo = create("div", classes='output alert alert-primary fade show')
    messageinfo.element.innerText = 'Message: ' '\n' + messageout
    div.element.appendChild(messageinfo.element)

    namein.clear()
    emailin.clear()
    phonein.clear()
    messagein.clear()
   
button.element.onclick = getthethings