"""Line_Follower_v1 controller."""
from controller import Camera
from controller import CameraRecognitionObject
from controller import Robot

def run_robot(robot):
    time_step = 32
    default_speed = 1
    max_speed = 1
    #Motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    
    IR_left = robot.getDevice('IR_left')
    IR_left.enable(time_step)
    IR_right = robot.getDevice('IR_right')
    IR_right.enable(time_step)
    cam = robot.getDevice('camera')
    cam.enable(time_step)
    geti = -1
    g = 0
    width = cam.getWidth()
    height = cam.getHeight()

    #Step simulation
    while robot.step(time_step)!= -1:
        
        
        #read sensors
        IR_left_value = IR_left.getValue()
        IR_right_value = IR_right.getValue()
        
        image = cam.getImageArray()
        left_sum = 0
        right_sum = 0  
       
        for x in range(0,25):
          for y in range(10,30):
            red   = image[x][y][0]
            green = image[x][y][1]
            blue  = image[x][y][2]
            gray  = (red + green + blue) / 3
            left_sum += gray
            
        for x in range(26,51):
           for y in range(10,30):
                    red   = image[x][y][0]
                    green = image[x][y][1]
                    blue  = image[x][y][2]
                    gray  = (red + green + blue) / 3
                    right_sum += gray
            
       
       
        if(IR_left_value > 5 and IR_right_value < 5):
            x = 0
            left_speed = max_speed  *0.0
            right_speed = max_speed  * 1.7
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
            x += 1
        elif(IR_right_value > 5 and IR_left_value < 5 ):
            x = 0
            left_speed = max_speed  * 1.7
            right_speed = max_speed * 0.0
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
            x += 1
                      
        else:
            left_speed = max_speed * 1.3
            right_speed = max_speed * 1.3
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)          
       # print("IRL:"+str(IR_left_value) +" IRR:"+str(IR_right_value))   
        
if __name__ == "__main__":
    #my_robot = Robot()
   # run_robot(my_robot)
    
    