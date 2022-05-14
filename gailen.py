from js import console

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

def showthethings(*args):
    #console.log('button was clicked')
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
   
button.element.onclick = showthethings