from graphics import *

class Wheel(object):

    def __init__( self, center, wheel_radius, tire_radius ):
        self.tire_circle = Circle( center, tire_radius )
        self.wheel_circle = Circle( center, wheel_radius )

    def draw( self, win ):
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    def move( self, dx, dy ):
        self.tire_circle.move( dx, dy )
        self.wheel_circle.move( dx, dy )

    def set_color( self, wheel_color, tire_color ):
        self.tire_circle.setFill( tire_color )
        self.wheel_circle.setFill( wheel_color )

    def undraw(self):
        self.tire_circle.undraw()
        self.wheel_circle.undraw()

    def get_center(self):
        return self.tire_circle.getCenter()

    def get_X(self):
        return self.tire_circle.getX

    def animate( self, win, dx, dy, n ):

        if n > 0:
            self.move( dx, dy )
        win.after( 100, self.animate, win, dx, dy, n - 1 ) 
            
        
if __name__ == '__main__':

    win = GraphWin( 'Wheel', 1200, 500 )

    win.setBackground( 'cyan' )

    myWheel = Wheel( Point( 50, 50 ), 30 , 40 )

    myWheel.set_color( 'yellow', 'black' )
 
    myWheel.draw( win )

    myWheel.animate( win, 5, 0, 200 )

    win.getMouse()
    win.close() 




