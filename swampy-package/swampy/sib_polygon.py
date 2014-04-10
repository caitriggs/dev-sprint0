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

def polyline(t, n, length, angle):
	for i in range(n):
	        fd(t, length)
	        lt(t, angle)

# Tells a turtle to draw an n-sided polygon
def polygon(t, length, n):
	angle = 360/n
	#could replace the next 3 lines with polyline()
	for i in range(n):
		fd(t, length)
		lt(t, angle)
		
polygon(bob, 50, 8)


wait_for_user()					
