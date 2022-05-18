from js import console, fetch

import sqlite3 as sql
import csv

from datetime import datetime
import random

### REFERENCE VIDEO https://www.youtube.com/watch?v=7meW2djIUYk&t=4s

### TODO - BUILD CONTACT FORM AND BLOG USING PYSCRIPT

#introduce tags to python
    #variable = Element('tag-id')
name = Element('name')
email = Element('email')
phone = Element('phone')
message = Element('message')
button = Element('submit')
bulb = Element('bulb')
    #<div class="pydiv"> for confirmation messages
div = Element('pydiv')
    #<div class="pydiv"> for lightbulb counter
bulbcounter = Element('bulbcounter')
counter = 0
def getthethings(*args):
    #console.log('button was clicked')
    timestamp = datetime.timestamp(datetime.now())
    nameout = name.element.value
    emailout = email.element.value
    phoneout = phone.element.value
    messageout = message.element.value

    confirmation = create("div", classes='output text-center alert alert-info fade show')
    confirmation.element.innerText = 'Your message has been sent.'
    div.element.appendChild(confirmation.element)

    userinfo = create("div", classes='output text-center alert alert-primary fade show')
    userinfo.element.innerText = nameout + '\n' + emailout + '\n' + phoneout
    div.element.appendChild(userinfo.element)

    messageinfo = create("div", classes='output alert alert-primary fade show')
    messageinfo.element.innerText = 'Message: ' '\n' + messageout
    div.element.appendChild(messageinfo.element)

    name.clear()
    email.clear()
    phone.clear()
    message.clear()

def lightbulb(self):
    global counter
    counter += 1

    if counter <3:
        Element('bulbcounter').element.innerText = counter
    else:
        randstr = ['The code for this counter was written with pyscript', counter, counter, 'On or off?', counter, counter, 'Please stop playing with the light and look at the portfolio', counter, counter, counter, counter, "It seems like you're enjoying this", counter, counter, "Please don't break the bulb", counter, counter, counter, counter, counter, counter, 'Do you think this is a bit overkill for a darkmode switch?', counter, counter, counter, counter, counter, counter, '...blinded by the light...', counter, counter, 'The lights are on but nobody is home...', counter, counter, counter, counter, 'Did you know that Blinded by the Light was actually written by Springsteen?']
        Element('bulbcounter').element.innerText = random.choice(randstr)

    console.log(counter)


#button.element.onclick = getthethings
bulb.element.onclick = lightbulb