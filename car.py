from graphics import *     # import everything in the graphics module

from wheel import Wheel    # import the Wheel class from the wheel module



class Car:                 # Car class definition
    
    def __init__( self, back_wheel_pos, back_wheel_rad, front_wheel_pos, front_wheel_rad, car_height ): # constructor method to instantiate 
        self.back_wheel = Wheel( back_wheel_pos, back_wheel_rad, back_wheel_rad + 5 )                   # a class object
        self.front_wheel = Wheel( front_wheel_pos, front_wheel_rad, front_wheel_rad + 5 )               # attributes of the Car class are defined
        self.car_body = Rectangle( Point( back_wheel_pos.getX(), back_wheel_pos.getY() - car_height),   # and initialized
                              front_wheel_pos )
        self.car_color = ''

        self.Road_1 = Line( Point( 0, 100 ), Point( 1200, 100 ) )

        self.Road_2 = Line( Point( 0, 40 ), Point( 1200, 40 ) ) 
        
        

    def carMove( self, dx, dy ):              # function to effect motion of the car object
        self.back_wheel.move( dx, dy )        # by individually moving each item
        self.front_wheel.move( dx, dy )       
        self.car_body.move( dx, dy )

    def setColour( self, tireColour, wheelColour, carColour ):  # function to set the colour attribute of each item 
        self.back_wheel.set_color( wheelColour, tireColour )
        self.front_wheel.set_color( wheelColour, tireColour )
        self.car_body.setFill( carColour )

    def animate( self, win, dx, dy, n ):     # function to perform the animation. This function is looped by the 'after' function until n = 0
        if n > 0:
            self.carMove( dx, dy )
        win.after( 100, self.animate, win, dx, dy, n - 1 )

    def draw( self, win ):      # draw the car object by drawing each individual item. The last item drawn appears on the foreground
        self.car_body.draw( win )
        self.back_wheel.draw( win )
        self.front_wheel.draw( win )
        

win = GraphWin( 'Car', 1200, 500 )     # create the window within which the car object is contained.

car1 = Car( Point(50,50), 15, Point(100,50) ,15, 40 ) # create the car object

car1.Road_1.draw( win )

car1.Road_2.draw( win )

car1.draw( win )    # draw the car object

car1.setColour( 'black', 'grey', 'pink' )  # set the colour parameters of the car object

car1.animate( win, 3, 0, 200 )  # perform the animation to move the car along the screen

win.getMouse()  # wait for a mouse click
win.close()   # close after a mouse click
        
