import random  

### Put your images in this list. Use URL's if you're on CMU, and file paths if you're running locally.
image_urls = [] 
random.shuffle(image_urls) 

images = [ Image(url, 0, 0, visible = False) for url in image_urls ]

app.bracket = 0     
app.iteration = 0  
    
b1, b2, b3, b4, b5, b6, b7, b8, b9 = [], [], [], [], [], [], [], [], []
brackets = [images, b1, b2, b3, b4, b5, b6, b7, b8, b9]

currentBracketLabel = Label("Bracket 1", 200, 350, size = 15)

app.pairs = []
if len(images) %2 != 0: # Make sure there's an even number of images and move one image to the next bracket if there's an odd number
    brackets[app.bracket+1].append(images.pop(0))
for i in range(0, len(images)): # Put the images in pairs that the user will choose from
    if i %2 != 0:   
        pair = [images[i-1], images[i]]
        app.pairs.append(pair)
        
def newBracket(bracket): 
    
    app.pairs.clear()
    
    if len(brackets[bracket]) % 2 != 0 and len(brackets[bracket]) != 1: 
        brackets[bracket+1].append(brackets[bracket].pop(0))
        
    for i in range(0, len(brackets[bracket])): 
        
        if len(brackets[bracket]) == 1: 
            currentBracketLabel.visible = False
            brackets[bracket][0].centerX = 200
            brackets[bracket][0].centerY = 200
            for img in images: 
                img.visible = False
            brackets[bracket][0].visible = True
            
            for i in range(0, len(images)):          
                if images[i] == brackets[bracket][0]:
                    Label(image_urls[i].split("/")[len(image_urls[i].split("/"))-1] + " is the best", 200, 40, size = 20)
                    
        elif i % 2 != 0:    
            pair = [brackets[app.bracket][i-1], brackets[app.bracket][i]]
            app.pairs.append(pair)
    
    currentBracketLabel.value = "Bracket " + str(bracket + 1) 
    app.iteration = 0   
    showPair()  

def showPair():
    
    if len(brackets[app.bracket]) == 1: # Don't do anything if the very last image is chosen
        pass
    
    elif app.iteration + 1 > len(app.pairs): # Move on to the next bracket if the last pair in the current bracket was decided
        app.bracket += 1
        newBracket(app.bracket)

    else:       # Display the pair; make all the images invisible and only show the 2 images in the pair
        for img in images:          
            img.visible = False
        app.pairs[app.iteration][0].visible = True
        app.pairs[app.iteration][1].visible = True
        app.pairs[app.iteration][0].centerX = 100
        app.pairs[app.iteration][0].centerY = 200
        app.pairs[app.iteration][1].centerX = 300
        app.pairs[app.iteration][1].centerY = 200
        app.iteration += 1

def onMousePress(x, y):
    for img in brackets[app.bracket]:
        if (img.hits(x, y)) and (img.visible == True):  # If the image is clicked on, add it to the next bracket
            brackets[app.bracket+1].append(img)
            showPair()
            break

showPair() 
