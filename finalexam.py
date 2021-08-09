#################################################
# hw7: One-Dimensional Connect Four
# name:Michael Kosecki
# andrew id: mkosecki
#
# 
#################################################

import cs112_n21_week3_linter
from cmu_112_graphics import *
import random, string, math, time

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
#################################################
# main app
#################################################

def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'
     
def gameDimensions():
    rows=40
    cols=20
    cellSize=20
    margin=25
    gamedimensions=[rows,cols,cellSize,margin]
    return(gamedimensions)

def make2dList(rows, cols,number):
    return [ ([number] * cols) for row in range(rows) ]

def appStarted(app):
    app.row,app.col,app.cellwidth,app.margin=gameDimensions()
    app.mines=make2dList(app.row,app.col,0)
    app.mines=mines(app)
    app.gameover=False
    app.revealed=make2dList(app.row,app.col,100)
    pass

def mines(app):
    mines=0
    list=[]
    for i in range(app.row):
        for j in range(app.col):
            list.append([i,j])
    while mines<160:
        b=len(list)-1
        a=random.randint(0,b)
        x,y=list[a]
        mines=mines+1
        app.mines[x][y]=-1
        list.pop(a)
    return app.mines

def getCellBounds(app,col,row):
    x0=app.margin+col*app.cellwidth
    y0=app.margin+row*app.cellwidth
    x1=app.margin+(col+1)*app.cellwidth
    y1=app.margin+(row+1)*app.cellwidth
    return(x0,y0,x1,y1)

def surroundingmines(app,x,y):
    count=0
    for i in range(3):
        for j in range(3):
            a=x-1+i
            b=y-1+j
            if(a<len(app.mines)):
                if(b<len(app.mines[i])):
                    if(a>=0):
                        if(b>=0):
                            if(app.mines[a][b]==-1):
                                count=count+1                
    return count

def revealspace(app,x,y):
    if(app.revealed[x][y]==100):
        app.revealed[x][y]=(surroundingmines(app,x,y))
        if(surroundingmines(app,x,y)==0):
            for i in range(3):
                for j in range(3):
                    a=x-1+i
                    b=y-1+j
                    if(a<len(app.mines)):
                        if(b<len(app.mines[i])):
                            if(a>=0):
                                if(b>=0):
                                    if(app.mines[a][b]!=-1):
                                        revealspace(app,a,b)
    pass

def mousePressed(app, event):
    x=(event.x-app.margin)//app.cellwidth
    y=(event.y-app.margin)//app.cellwidth
    if(app.margin<event.x<app.margin+app.cellwidth*app.row):
        if(app.margin<event.y<app.margin+app.cellwidth*app.col):
            if(app.mines[x][y]==-1):
                app.revealed[x][y]=-1
            elif(surroundingmines(app,x,y)>0):
                app.revealed[x][y]=surroundingmines(app,x,y)
            else:
                revealspace(app,x,y)
    pass

def gameover(app):
    pass

def keyPressed(app, event):
    if(event.key=="p"):
        pass
    pass

def redrawAll(app, canvas):
    drawGrid(app,canvas)
    drawRevealed(app,canvas)
 #   drawmenu(app,canvas)
    pass

#def drawmenu(app,canvas):
 #   if(app.menu==True):
 #       canvas.create_rectangel(0,0,app.width,app.height):
        

def drawRevealed(app,canvas):
    for i in range(len(app.revealed)):
        for j in range(len(app.revealed[i])):
            if app.revealed[i][j]==0:
                canvas.create_rectangle(getCellBounds(app,i,j),fill="white")
            elif app.revealed[i][j]>0:
                if(app.revealed[i][j]<9):
                    canvas.create_rectangle(getCellBounds(app,i,j),fill="white")
                    canvas.create_text(app.margin+(i+.5)*app.cellwidth,
                    app.margin+(j+.5)*(app.cellwidth),text=app.revealed[i][j]) 
            elif app.revealed[i][j]==-1:
                canvas.create_oval(getCellBounds(app,i,j),
                fill=rgbString(150,150,150))

def drawGrid(app, canvas):
    for i in range(len(app.mines)):
        for j in range(len(app.mines[i])):
            fill=rgbString(0,0,255)
            canvas.create_rectangle(getCellBounds(app,i,j),fill=fill)    
    pass


def runMinesweeper():
    rows,cols,cellSize,margins=gameDimensions()
    width=rows*cellSize+2*margins
    height=cols*cellSize+2*margins
    runApp(width=width,height=height)


def main():
    cs112_n21_week3_linter.lint()
    runMinesweeper()

if __name__ == '__main__':
    main()