"""Line_Follower_v1 controller."""
"""Importowanie biblioteki applikacji Webots z funkcjami dla kontroli robota
    Zakomentowałem biblioteki """
from controller import Camera
from controller import CameraRecognitionObject
from controller import Robot

"""Funkcja z kodem dla opracowania działania robota"""
def run_robot(robot):
    time_step = 32
    default_speed = 1
    max_speed = 1
    """Włączenie motorów kołek robota"""
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

    """Włączenie czujników robota"""
    IR_left = robot.getDevice('IR_left')
    IR_left.enable(time_step)
    IR_right = robot.getDevice('IR_right')
    IR_right.enable(time_step)

    """Włączenie kamery robota"""
    cam = robot.getDevice('camera')
    cam.enable(time_step)
    geti = -1
    g = 0
    width = cam.getWidth()
    height = cam.getHeight()

    """Symulacja czasu"""
    while robot.step(time_step)!= -1:
        
        
       """Odczytywanie wartości czujników"""
       IR_left_value = IR_left.getValue()
       IR_right_value = IR_right.getValue()

       """Odczytanie obrazu kamery"""
       image = cam.getImageArray()
       left_sum = 0
       right_sum = 0

       """Analiza pikseli pobranego obrazku i wyliczzanie szarości każdej połówy"""
       """Prawej"""
       for x in range(0,25):
          for y in range(20,30):
            red   = image[x][y][0]
            green = image[x][y][1]
            blue  = image[x][y][2]
            gray  = (red + green + blue) / 3
            left_sum += gray
       """Oraz lewej"""
       for x in range(26,52):
           for y in range(20,30):
                    red   = image[x][y][0]
                    green = image[x][y][1]
                    blue  = image[x][y][2]
                    gray  = (red + green + blue) / 3
                    right_sum += gray
            
       """Zmniejszenie wyliczonej wartości dla wygodnego korzystania"""
       left_sum = left_sum / 1000
       right_sum = right_sum / 1000

       """Kontrola szybkości w zależności od wyniku obliczeń szarości"""
       if ( right_sum < 30 or left_sum < -30):
               max_speed = default_speed * 1.5
       elif ( right_sum < 20 or left_sum < 20):
               max_speed = default_speed * 0.3
       elif ( right_sum > 40 or left_sum > 40):
               max_speed = default_speed * 3.5
       else:
            max_speed = default_speed

       
       """Analizując wartości otrzymane od czujników oraz średnią szarość 
       otrzymaną po analizie obrazu z kamery
       program decyduje czy robot musi skrecać"""
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
       elif(IR_right_value == 1000 and IR_left_value  == 1000):
            left_speed = max_speed  * 1.7
            right_speed = max_speed * 0.0
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
       elif(IR_right_value >5 and IR_left_value >5  and left_sum <80 and right_sum < 80):
            left_speed = max_speed
            right_speed = max_speed
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
       elif(left_sum >110 and right_sum > 110):
            left_speed = max_speed  * 1.7
            right_speed = max_speed * 0.0
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
       elif(IR_right_value >5 and IR_left_value >5  and left_sum > right_sum):
            left_speed = max_speed  * 1.7
            right_speed = max_speed * 0.0
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
       elif(IR_right_value >5 and IR_left_value >5 and left_sum < right_sum):
            left_speed =max_speed * 0.0
            right_speed =  max_speed  * 1.7
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
                      
       else:
            left_speed = max_speed
            right_speed = max_speed
       left_motor.setVelocity(left_speed)
       right_motor.setVelocity(right_speed)


"""Funkcja 'main' włącza robota oraz wywołuje funkcje 'run_robot'"""
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
    
    