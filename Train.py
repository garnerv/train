#  File: Train.py

#  Description: A program that will draw a train using turtle graphics

#  Student Name: Garner Vincent

#  Student UT EID: GV4353

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 2-16-15

#  Date Last Modified: 2-19-15

import turtle, math

#this function draws the rails that the train rides on
def drawRail(ttl, lent, wid, x, y):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.goto(x, y - wid)
	ttl.goto(x + lent, y - wid)
	ttl.goto(x + lent, y)
	ttl.penup()
	return(drawStuds(ttl, x, y))

#this function passes between the draw rail function to draw the stuts onto the train tack
def drawStuds(ttl, x, y):
	if (x > 250):
		return
	else:
		return(drawRail(ttl, 20, 5, x + 40, y))

#this funciton draws the horizontal circle bolts on on the rectangles on the train
def drawBoltsVert(ttl, x, y, size):
	if (x > 310):
		return
	else:
		return(drawCircleBoltsVert(ttl, x, y, size))

#this funciton draws the horizontal circle bolts on on the rectangles on the train
def drawCircleBoltsVert(ttl, x, y, size):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.begin_fill()
	ttl.circle(size)
	ttl.end_fill()
	ttl.penup()
	return (drawBoltsVert(ttl, x + 10, y, size))


#this funciton draws the vertical circle bolts on on the rectangles on the train
def drawBoltsHor(ttl, x, y, size):
	if (y > 102):
		return
	else:
		return(drawCircleBoltsHor(ttl, x, y, size))

#this funciton draws the vertical circle bolts on on the rectangles on the train
def drawCircleBoltsHor(ttl, x, y, size):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.begin_fill()
	ttl.circle(size)
	ttl.end_fill()
	ttl.penup()
	return (drawBoltsHor(ttl, x, y + 10, size))

#draws a line from one point to another
def drawLine(ttl, x, y, x2, y2):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.goto(x2, y2)
	ttl.penup()

#draws a circle of a given size
def drawCircle(ttl, x, y, dim):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(dim)
	ttl.penup()

#draws any shape of a given step count
def drawShape(ttl, x, y, dim, stp):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(dim, steps = stp)
	ttl.penup()

#draws an arc
def arc (ttl, x, y, size, degrees):
	ttl.goto(x, y)
	ttl.pendown()
	for iter in range (degrees):
		ttl.forward(size)
		ttl.right(1)
	ttl.penup()

#draws a rectangle
def drawRectangle(ttl, x, y, length, width):
	drawLine(ttl, x, y, x + length, y)
	drawLine(ttl, x + length, y, x + length, y + width)
	drawLine(ttl, x + length, y + width, x, y + width)
	drawLine(ttl, x, y + width, x, y)

#draw spokes with a middle circle
def drawSpoke(ttl, x, y, spokeSize):
	degrees = 360
	ttl.goto(x, y)
	ttl.pendown()
	if spokeSize == .25:
		for iter in range (degrees):
			if (iter % 45 == 0):
				ttl.left(100)
				ttl.forward(30)
				ttl.backward(30)
				ttl.right(100)
				ttl.left(80)
				ttl.forward(30)
				ttl.backward(30)
				ttl.right(80)
			ttl.forward(spokeSize)
			ttl.right(1)
	elif spokeSize == .15:
		for iter in range (degrees):
			if (iter % 45 == 0):
				ttl.left(100)
				ttl.forward(26.5)
				ttl.backward(26.5)
				ttl.right(100)
				ttl.left(80)
				ttl.forward(26.5)
				ttl.backward(26.5)
				ttl.right(80)
			ttl.forward(spokeSize)
			ttl.right(1)
	ttl.penup()

#will draw the inner and outer part of the wheel with the spoke function
def drawWheels(ttl, x, y, radius, spokeSize):
	drawCircle(ttl, x, y, radius)
	drawCircle(ttl, x, y + 10, radius - 10)
	if radius == 55:
		drawSpoke(ttl, x, y + (radius + 15), spokeSize)
	elif radius == 45:
		drawSpoke(ttl, x, y + (radius + 7.5), spokeSize)


def main():
  # put label on top of page
  turtle.title ('Train')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  #create turtle object
  ttl1 = turtle.Turtle()
  ttl1.pensize(2)

  #draw rail
  drawLine(ttl1, -350, -200, 350, -200)
  drawLine(ttl1, -350, -220, 350, -220)
  drawStuds(ttl1, -350, -220)

  #create turtle object number2
  ttl2 = turtle.Turtle()
  ttl2.pensize(2)

  #draw wheels
  ttl2.color('red')
  drawWheels(ttl2, -200, -200, 55, .25)
  drawWheels(ttl2, 20.74, -200, 45, .15)
  drawWheels(ttl2, 214.26, -200, 45, .15)

  #draw wheel arc with side splits
  ttl2.color('blue')

  #back of train body
  drawLine(ttl2, -300, 150, -300, -150)
  drawLine(ttl2, -300, -150, -272.5, -150)
  ttl2.left(90)
  arc(ttl2, -272.5, -150, 1.25, 180)
  ttl2.left(90)
  ttl2.pendown()
  ttl2.forward(27.5)
  ttl2.left(90)
  ttl2.forward(300)
  ttl2.left(90)
  ttl2.forward(197)
  drawRectangle(ttl2, -330, 151, 260, 40)

  #top main train body
  drawLine(ttl2, -101.76, 110, 312.20, 110)
  drawRectangle(ttl2, 30, 110, 70, 25)
  drawRectangle(ttl2, 50, 135, 30, 12)

  #draw smokestack 
  drawLine(ttl2, 190, 110, 160, 196.6)
  ttl2.goto(160, 196.6)
  ttl2.pendown()
  ttl2.right(180)
  ttl2.forward(100)
  ttl2.left(120)
  ttl2.forward(30)
  ttl2.left(60)
  ttl2.forward(70)
  ttl2.left(60)
  ttl2.forward(30)

  ttl2.penup()
  ttl2.right(60)
  drawLine(ttl2, 230, 110, 260, 196.6)


  #bottom train body
  ttl2.goto(-101.76, -149)
  ttl2.penup()
  ttl2.right(180)
  ttl2.pendown()
  ttl2.forward(50)
  ttl2.left(90)
  arc(ttl2, -51.76, -148.75, 1.25, 180)
  ttl2.pendown()
  ttl2.left(90)
  ttl2.forward(50)
  ttl2.left(90)
  arc(ttl2, 141.76, -148.46, 1.25, 180)
  ttl2.left(90)
  ttl2.pendown()
  ttl2.forward(27.5)
  ttl2.penup()
  drawLine(ttl2, 312.20, -147.21, 312.20, 110)

  #draw steel bolt tracks
  drawRectangle(ttl2, -102, -5, 414, 15)
  drawBoltsVert(ttl2, -96, 0, 2)

  drawRectangle(ttl2, -10, 10, 15, 100)
  drawBoltsHor(ttl2, -3, 16, 2)
  drawRectangle(ttl2, 207, 10, 15, 100)
  drawBoltsHor(ttl2, 214, 16, 2)

  #draw polygon thing on front of train
  ttl2.penup()
  ttl2.goto(312.50, -147.21)
  ttl2.pendown()
  ttl2.forward(60)
  ttl2.left(120)
  ttl2.forward(60)
  ttl2.left(60)
  ttl2.forward(30)

  #draw rectangles on front of train
  drawRectangle(ttl2, 312.20, -70, 20, 150)
  drawRectangle(ttl2, 332.20, -35, 10, 75)

  #draw windows in caboose
  ttl2.color('gray')
  ttl2.begin_fill()
  drawRectangle(ttl2, -280, 40, 70, 80)
  ttl2.end_fill()
  ttl2.begin_fill()
  drawRectangle(ttl2, -190, 40, 70, 80)
  ttl2.end_fill()

  ttl2.color('blue')
  drawRectangle(ttl2, -280, 40, 70, 80)
  drawRectangle(ttl2, -190, 40, 70, 80)


  # hide ttl
  ttl2.hideturtle()
  # persist drawing
  turtle.done()

main()
