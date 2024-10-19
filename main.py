#import os
#import time
from spot_controller import SpotController
from bosdyn.client.robot_command import RobotCommandBuilder

#import math
# import cv2

ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']

def degrees_to_radians(angle_degrees):
    """Convert degrees to radians without using the math module."""
    pi = 3.14159265358979323846264338  # Approximate value of pi
    return angle_degrees * (pi / 180.0)



def turn_spot(spot, angle_degrees):
    """
    Turn Spot by the specified angle in degrees.
    
    Positive angle turns right (clockwise), negative angle turns left (counterclockwise).
    """
    angle_radians = degrees_to_radians(angle_degrees)
    rotate_command = RobotCommandBuilder.synchro_se2_trajectory_point_command(
        goal_x=0.0,
        goal_y=0.0,
        goal_heading=angle_radians,  # Positive is Right, Negative is Left
        frame_name='body'
    )

    spot.command_client.robot_command(rotate_command)

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

def run():

    flag = False

    while True:
        x = input("What do you want the dog to do? :" )
        with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:
            #time.sleep(2)
#         capture_image()
#         # Move head to specified positions with intermediate time.sleep
            if not flag:
                spot.move_head_in_points(yaws=[0.2, 0], pitches=[0.3, 0],  rolls=[0.4, 0],sleep_after_point_reached=1)
#         capture_image()
            flag = True
#         time.sleep(3)
            #time.sleep(2)
            # Move head to specified positions with intermediate time.sleep

            if x == "q":
                break
                
            elif x == "w":
                spot.move_to_goal(goal_x=0.5, goal_y=0)
            elif x == "s":
                spot.move_by_velocity_control(v_x=-0.5, v_y=-0, v_rot=0, cmd_duration=3)
            elif x == "a":
                turn_spot(spot, -90)
            elif x == "d":
                turn_spot(spot, 90)


if __name__ == '__main__':
    run()

