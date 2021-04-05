'''
This is a sample class that you can use to control the mouse pointer.
It uses the pyautogui library. You can set the precision for mouse movement
(how much the mouse moves) and the speed (how fast it moves) by changing 
precision_dict and speed_dict.
Calling the move function with the x and y output of the gaze estimation model
will move the pointer.
This class is provided to help get you started; you can choose whether you want to use it or create your own from scratch.
'''
import pyautogui

class MouseController:
    def __init__(self, precision, speed):
        precision_dict={'high':10, 'low':1000, 'medium':500}
        speed_dict={'fast':0.0, 'slow':10, 'medium':5}

        self.precision=precision_dict[precision]
        self.speed=speed_dict[speed]
        screen_size=pyautogui.size()
        pyautogui.moveTo(screen_size[0]/2,screen_size[1]/2)

    def move(self, x, y):
        screen_pos=pyautogui.position()
        self.print_position(screen_pos[0]+x*self.precision, screen_pos[1]+-1*y*self.precision)
        if pyautogui.onScreen(screen_pos[0]+x*self.precision, screen_pos[1]+-1*y*self.precision):
            pyautogui.moveRel(x*self.precision, -1*y*self.precision, duration=self.speed)

    def print_position(self, x,y):
        #x, y = pyautogui.position()
        positionStr = 'X: {0} Y: {1}'.format(str(x).rjust(4), str(y).rjust(4))
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
