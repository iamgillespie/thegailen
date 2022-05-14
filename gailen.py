from js import console

### REFERENCE VIDEO https://www.youtube.com/watch?v=7meW2djIUYk&t=4s

### TODO - BUILD CONTACT FORM AND BLOG USING PYSCRIPT

#introduce tags to python
    #<input type="text" id="pyinput" class="form-control" placeholder="Enter some text">
pyinput = Element('pyinput')
    #<button type="button" class="btn btn-light" id="submit">Submit</button>
button = Element('submit')
    #<div class="pydiv">
div = Element('pydiv')

def showthethings(*args):
    #console.log('button was clicked')
    output = pyinput.element.value
    newthing = create("p", classes='output text-center')
    newthing.element.innerText = output
    div.element.appendChild(newthing.element)

    pyinput.clear()
   

button.element.onclick = showthethings