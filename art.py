from PIL import Image
import PIL
import turtle
from random import shuffle

im_location = ""
pdif_num = 20
col  = "B"
colors = {
    "B": "black",
    "R": "red",
    "Y": "yellow",
    "G": "green",
    "BL": "blue"
}

def get_image():
    global im_location
    im_location = input("image location:")
    im = Image.open(im_location)
    x_size,y_size = im.size
    max_size = int(input("max size (recomended 60):"))
    k = max(x_size,y_size)/max_size
    x_size= int(x_size/k)
    y_size= int(y_size/k)

    im = im.resize((x_size, y_size), PIL.Image.ANTIALIAS)

    x_size,y_size = im.size
    p = im.load() # pixels of image 
    
    global pdif_num
    pdif_num = int(input("sharpness [0..768] (recomended 50):"))

    return (x_size, y_size, p)

def pdif(p1, p2):
    # absolute difference between pixels
    global pdif_num
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2]) > pdif_num

def paint1():
    scr_size = 500
    x_size, y_size, p = get_image()
    scr = turtle.Screen()
    turtle.screensize(scr_size, scr_size)  
    artist = turtle.Turtle()
    artist.speed(0)

    points = []
    
    zoom = max(scr_size/x_size, scr_size/y_size)/2
    zoom_x = zoom
    zoom_y = zoom
    
    pl_x = -250
    pl_y = 250
    
    zoom_y *= -1

    global col
    artist.pen(pencolor=col, pensize=2)
    

    for x in range(x_size):
        for y in range(y_size):
            if (x>0 and pdif(p[x,y],p[x-1,y])) or (y>0 and pdif(p[x,y],p[x,y-1])):
                points.append((x*zoom_x,y*zoom_y))

    shuffle(points)

    for x,y in points:
        artist.pu()
        artist.goto(pl_x+x,pl_y+y)
        artist.pd()
        for t in range(5):
            artist.forward(zoom/2)
            artist.left(360.0/5)


def paint2():
    scr_size = 500
    x_size, y_size, p = get_image()
    scr = turtle.Screen()
    turtle.screensize(scr_size, scr_size)  
    artist = turtle.Turtle()
    artist.speed(0)

    global col
    artist.pen(pencolor=col, pensize=2)

    points = []
    
    zoom = max(scr_size/x_size, scr_size/y_size)/2
    zoom_x = zoom
    zoom_y = zoom
    
    pl_x = -250
    pl_y = 250

    zoom_y *= -1
    

    for x in range(x_size):
        for y in range(y_size):
            if (x>0 and pdif(p[x,y],p[x-1,y])) or (y>0 and pdif(p[x,y],p[x,y-1])):
                points.append((x*zoom_x,y*zoom_y))

    shuffle(points)


    for x,y in points:
        l = []
        for xx,yy in points:
            if abs(x-xx) + abs(y-yy) < 18:
                l.append((abs(x-xx) + abs(y-yy),(xx,yy)))
        l = sorted(l)
        for w in l[:10]:
            xx,yy = w[1]
            artist.pu()
            artist.goto(pl_x+x,pl_y+y)
            artist.pd()
            artist.goto(pl_x+xx,pl_y+yy)


def paint3():
    RN = int(input("Numer of rows in pascal Triangle (1-10):"))

    scr_size = 500
    scr = turtle.Screen()
    turtle.screensize(scr_size, scr_size)  
    artist = turtle.Turtle()
    artist.speed(0)
    global col
    artist.pen(pencolor=col, pensize=3)
    
    
    D = 400 / (1.5 * RN)

    F = D / 3

    A = [1]

    for t in range(1,RN+1):

        y = 200 - (len(A)-1)* 1.5 * D

        x = 0

        for i in range(len(A)):
            if len(A) % 2 == 1:
                x = D*3**0.5 * ((len(A)-1)/2 - i)
            else:
                x = D*3**0.5 * ((len(A))/2 - i) - D*3**0.5/2  

            artist.pu()
            artist.goto(x,y-F/2)
            
            artist.write(str(A[i]), True, align="center", font=("Arial", int(F), "bold"))
            
            artist.goto(x,y)
            
            artist.seth(90)
            artist.forward(D)
            artist.left(120)
            artist.pd()
            for tt in range(6):
                artist.forward(D)
                artist.left(60)

        B = [1]
        for y in range(1,len(A)):
            B.append(A[y-1]+A[y])
        B.append(1)
        A = B



if __name__ == "__main__":
    col = colors[input("colors  B(black), R(red), Y(yellow), BL(blue) or G(green):")] 
    paint_type = input("paint type A, B or C:")
    if paint_type == "A":
        paint1()
    if paint_type == "B":
        paint2()
    if paint_type == "C":
        paint3()
    input()