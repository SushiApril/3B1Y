#import os
#import time
from spot_controller import SpotController
from bosdyn.client.robot_command import RobotCommandBuilder
import time

#import math
# import cv2

ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']

def degrees_to_radians(angle_degrees):
    """Convert degrees to radians without using the math module."""
    pi = 3.14159265358979323846264338  # Approximate value of pi
    return angle_degrees * (pi / 180.0)


# def capture_image():
#     camera_capture = cv2.VideoCapture(0)
#     rv, image = camera_capture.read()
#     print(f"Image Dimensions: {image.shape}")
#     camera_capture.release()


# def main():
#     #example of using micro and speakers
#     print("Start recording audio")
#     sample_name = "aaaa.wav"
#     cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=10 -c 1 {sample_name}'
#     print(cmd)
#     os.system(cmd)
#     print("Playing sound")
#     os.system(f"ffplay -nodisp -autoexit -loglevel quiet {sample_name}")

#     # # Capture image

#     # Use wrapper in context manager to lease control, turn on E-Stop, power on the robot and stand up at start
#     # and to return lease + sit down at the end
#     with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:

#         time.sleep(2)
#         capture_image()
#         # Move head to specified positions with intermediate time.sleep
#         spot.move_head_in_points(yaws=[0.2, 0],
#                                  pitches=[0.3, 0],
#                                  rolls=[0.4, 0],
#                                  sleep_after_point_reached=1)
#         capture_image()
#         time.sleep(3)

#         # Make Spot to move by goal_x meters forward and goal_y meters left
#         spot.move_to_goal(goal_x=1.0, goal_y=0.5)
#         time.sleep(3)
#         capture_image()

#         # Control Spot by velocity in m/s (or in rad/s for rotation)
#         spot.move_by_velocity_control(v_x=-0.5, v_y=-0.3, v_rot=0, cmd_duration=3)
#         capture_image()
#         time.sleep(3)

def velocity_cmd_helper(spot, v_x=0.0, v_y=0.0, v_rot=0.0):
    """Helper to send velocity commands to Spot."""
    spot._start_robot_command(RobotCommandBuilder.synchro_velocity_command(v_x=v_x, v_y=v_y, v_rot=v_rot), end_time_secs=time.time() + 10)

# Movement methods
def move_forward(spot):
    spot.move_to_goal(goal_x=0.5, goal_y=0.0)

def move_backward(spot):
    spot.move_to_goal(goal_x=-0.5, goal_y=0.0)

def turn_left(spot):
    spot.move_by_velocity_control(v_x=-0.5, v_y=0.5, v_rot=0.8, cmd_duration=3)

def turn_right(spot):
    spot.move_by_velocity_control(v_x=-0.5, v_y=-0.5, v_rot=1.6, cmd_duration=3)

def strafe_left(spot):
    velocity_cmd_helper(spot, v_y=0.5)

def strafe_right(spot):
    velocity_cmd_helper(spot, v_y=-0.5)



def run():

    flag = False

    for i in range(5):
        x = input("What do you want the dog to do? :" )
        with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:
#         time.sleep(2)
#         capture_image()
#         # Move head to specified positions with intermediate time.sleep
            if not flag:
                spot.move_head_in_points(yaws=[0.2, 0], pitches=[0.3, 0],  rolls=[0.4, 0],sleep_after_point_reached=1)
#         capture_image()
            flag = True
#         time.sleep(3)
            #time.sleep(2)
            # Move head to specified positions with intermediate time.sleep

            if x == "quit":
                break
            elif x == "w":
                move_forward(spot)
            elif x == "s":
                move_backward(spot)
            elif x == "a":
                turn_left(spot)
            elif x == "d":
                turn_right(spot)
            else:
                print("bruh wrong command")


if __name__ == '__main__':
    run()

