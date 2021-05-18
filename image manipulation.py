import graphics
from graphics import *

def stat(image): 
    #kidus degefu
    print("stats button has been pressed")
    print("image stats....")
    print("calculating image histogram")
    
    #initializes the count and colors   
    count=0 	
    mred=0
    mgreen=0
    mblue=0
    nred=[]
    ngreen=[]
    nblue=[]
    occred=[]
    occgreen=[]
    occblue=[]

    #we made a list of each colors then arranged it in accending order
    #calculate the mean too	
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):
            r, g, b = image.getPixel(row,col)
            nred.append(r)
            nblue.append(b)
            ngreen.append(g)
            mred+= r
            mgreen+=g
            mblue+=b
            count+=1
            
    #sorts the nummber of pixles in each colors in accending order       
    nred.sort();	
    ngreen.sort();	
    nblue.sort()
    
    #prints total number of pixels and mean o each colors
    print("red mean : ", mred/count )
    print("green mean : ", mgreen/count )
    print("blue mean : ", mblue/count)
    print("Number of pixels is ",count)
            
        
    
def openImage(picFile,win):
    img = Image(Point(400, 350), picFile)
    width = img.getWidth()
    height = img.getHeight()
    img.draw(win)
    return img
def convertToNegative(image):
    print("Converting to color negative...")
    for col in range(image.getHeight()):
        for row in range(image.getWidth()): 
            
            #acquires the pixles from the image
            r, g, b = image.getPixel(row,col)
            
            #sets new(negative) pixles to the image
            image.setPixel(row,col, color_rgb(255-r,255-g,255-b))
        update()
    print("   ...Done.")

def convertToGrayscale(img):
    #kidus degefu
    print("Converting to grayscale...")
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            
            #acquires the pixles from the image
            (r, g, b) = img.getPixel(row,col)
            
            #sets new pixles for the image
            average = (int((r + g + b) / 3))
            img.setPixel(row, col, color_rgb(average, average, average))

        update()
    print("   ...Done.")

def bminus(image):
    br=25 
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):     
            r, g, b = int(image.getPixel(row,col))
            r-=br
            g-=br
            b-=br
            if r>255:
                r=255
            if g>255:
                g=255
            if b>255:
                b=255
            if r<0:
                r=0
            if g<0:
                g=0
            if b<0:
                b=0                
            image.setPixel(row,col, color_rgb(r,g,b))
        update()
    print("   ...Done.")
    
    
def bplus(image):
    br=25
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):     
            r, g, b = image.getPixel(row,col)
            r+=br
            g+=br
            b+=br
            if r>255:
                r=255
            if g>255:
                g=255
            if b>255:
                b=255
            if r<0:
                r=0
            if g<0:
                g=0
            if b<0:
                b=0                
            image.setPixel(row,col, color_rgb(r,g,b))
        update()
    print("   ...Done.")
    
def buttons(win):
    #the next lines of code create bbuttons in boxes and texts
    r1=Rectangle(Point(10,5),Point(150,45))
    r2=Rectangle(Point(160,5),Point(300,45))
    r3=Rectangle(Point(310,5),Point(450,45))
    r41=Rectangle(Point(460,5),Point(520,45))
    r42=Rectangle(Point(530,5),Point(590,45))
    r5=Rectangle(Point(680,5),Point(780,45))
    r6=Rectangle(Point(600,5),Point(670,45))
    r1.draw(win)
    r2.draw(win)
    r3.draw(win)
    r41.draw(win)
    r42.draw(win)
    r5.draw(win)
    r6.draw(win)
    o1=Text(Point(80,25),"image stat")
    o2=Text(Point(230,25),"negative")
    o3=Text(Point(380,25),"gray scale")
    o41=Text(Point(480,25)," b +")
    o42=Text(Point(560,25)," b -")
    o5=Text(Point(730,25),"quit")
    o6=Text(Point(635,25),"save")
    o1.draw(win)
    o2.draw(win)
    o3.draw(win)
    o41.draw(win)
    o42.draw(win)
    o5.draw(win)
    o6.draw(win)
def keyhandle(k,win,image):
    
    if k=="q":
        win.close()
    elif k=="b":
        adjustb() 
    elif k=="g":
        convertToGrayscale(image)
    elif k=="s":
        stats(image)
    elif k=="n":
        convertToNegative(image)
def save(image):
    #kidus degefu
    #saves the image with ppm format
    image.save("fs.ppm")
    
def mousehandle(p,win,image):
    #samuel
    x=p.getX()
    y=p.getY()
    if 10<=x<=150 and 5<=y<=45 :
        stat(image)
    elif 160<=x<=300 and 5<=y<=45:
        convertToNegative(image)
    elif 310<=x<=450 and 5<=y<=45:
        convertToGrayscale(image)
    elif 460<=x<=520 and 5<=y<=45:
        bplus(image)
    elif 530<=x<=590 and 5<=y<=45:
        bminus(image)        
    elif 600<=x<=670 and 5<=y<=45:
        save(image)
    elif 680<=x<=780 and 5<=y<=45:
        win.close()
def main(): 
    # kidus degefu
    win= GraphWin("Image Processer",800,600)
    
    #prompts the user to input an image file
    infile = input("Enter the name of a GIF or PNG file to convert: ")
    image=openImage(infile,win)
    buttons(win)
    while "t":
        key=win.checkKey()
        if key:
           keyhandle(key,win,image)
        mouse=win.checkMouse()
        if mouse:
           mousehandle(mouse,win,image)

    print()
    print("Done")
main()
    
    
        
