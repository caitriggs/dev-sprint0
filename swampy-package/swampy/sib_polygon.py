# Polygon exercise from Week 0

# Name: Caitlin 


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# Tells a turtle to draw a square
def square(t, angle, length):
    for i in range(4):
		fd(t, length)
		lt(t, angle)

square(bob, 90, 10)

# Tells a turtle to draw a n-sided polygon
def polygon(t, length, n):
	angle = 360/n
	for i in range(n):
		fd(t, length)
		lt(t, angle)
		
polygon(bob, 50, 8)



wait_for_user()					
