import re
import signal
import sys

from toy_robot import commands

global first_cmd
first_cmd = True


def _shutting_down(signum, frame):
    print ("INFO:Shutting down.")
    sys.exit(0)


def start_simulation():
    ''' Start simulator and wait for the next command

    '''

    signal.signal(signal.SIGTERM, _shutting_down)
    signal.signal(signal.SIGINT, _shutting_down)
    print('''
#######################################################################
####### ####### #     #         ######  ####### ######  ####### #######
   #    #     #  #   #          #     # #     # #     # #     #    #
   #    #     #   # #           #     # #     # #     # #     #    #
   #    #     #    #            ######  #     # ######  #     #    #
   #    #     #    #            #   #   #     # #     # #     #    #
   #    #     #    #            #    #  #     # #     # #     #    #
   #    #######    #            #     # ####### ######  #######    #
#######################################################################
Enter command as follows:
PLACE X,Y,F:   Place robot at (0<=x<5),(0<=y<5) position facing NORTH, EAST, SOUTH or WEST.
               Example: PLACE 3,4,WEST
MOVE       :   Move the toy robot one unit forward in the direction it is currently facing.
LEFT       :   Rotate the robot 90 degrees left without changing the position of the robot.
RIGHT      :   Rotate the robot 90 degrees right without changing the position of the robot.
REPORT     :   Announce the X,Y and F of the robot.

''')
    for line in sys.stdin:
        valid = re.match(r"(\w+)( (.*))?", line)
        if not valid:
            print ("ERROR: Invalid format for line: ", line)
            continue
        global first_cmd
        if first_cmd and valid.group(1) != "PLACE":
            print ("ERROR: First command must be PLACE")
            continue
        else:
            first_cmd = False

        commands.execute(valid.group(1),
                         valid.group(3).split(',') if valid.lastindex > 1 else [])


if __name__ == "__main__":
    start_simulation()
