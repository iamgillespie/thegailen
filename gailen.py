from js import console
import sqlite3 as sql
from datetime import datetime

### REFERENCE VIDEO https://www.youtube.com/watch?v=7meW2djIUYk&t=4s

### TODO - BUILD CONTACT FORM AND BLOG USING PYSCRIPT

#introduce tags to python
    #variable = Element('tag-id')
name = Element('name')
email = Element('email')
phone = Element('phone')
message = Element('message')
button = Element('submit')
    #<div class="pydiv">
div = Element('pydiv')

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

    con = sql.connect('gailen.db')
    con.row_factory = sql.Row
    cur = con.cursor()

    con.execute('INSERT INTO msgs (name, email, phone, message, timestamp) VALUES (?, ?, ?, ?, ?)', (nameout, emailout, phoneout, messageout, timestamp))
    con.commit()

    name.clear()
    email.clear()
    phone.clear()
    message.clear()
   
button.element.onclick = getthethings