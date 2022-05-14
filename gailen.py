from js import console

### REFERENCE VIDEO https://www.youtube.com/watch?v=7meW2djIUYk&t=4s

### TODO - BUILD CONTACT FORM AND BLOG USING PYSCRIPT

#introduce tags to python
    #variable = Element('tag-id')
name = Element('name')
email = Element('email')
message = Element('message')
button = Element('submit')
    #<div class="pydiv">
div = Element('pydiv')

def showthethings(*args):
    #console.log('button was clicked')
    nameout = name.element.value
    emailout = email.element.value
    messageout = message.element.value
    newthing = create("p", classes='output text-center')
    newthing.element.innerText = nameout + ' ' + emailout + ' ' + messageout
    div.element.appendChild(newthing.element)

    name.clear()
   

button.element.onclick = showthethings