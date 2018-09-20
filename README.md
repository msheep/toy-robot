# Toy Robot Simulator 🤖
### Overview
Toy Robot simulator application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.

### Description
- The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.
- There are no other obstructions on the table surface.
- Application accepts commands of the following form:
    - PLACE X,Y,F: will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
    - MOVE: will move the toy robot one unit forward in the direction it is currently facing.
    - LEFT and RIGHT: will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
    - REPORT: will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.
- A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT
  and REPORT commands.
- Input should be in the form of a text file or can be provided in interpreter mode.
- Test data to exercise the application are present in `tests/data/`
 
    ##### Constraints:

    - The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot.
    - Any move that would cause the robot to fall must be ignored.
### Prerequisites
- python3.6
- tox
### Installation and Running

1. Download/clone the project and change to the root folder of the project.
2. Install using following command command.
```sh
$ python setup.py install
```
3. Execute following command to run test
```sh
$ tox -epy36
```
4. And then excute the following command to run pep8 check
 ```sh
$ tox -epep8
```
5. Two way to run the application simulator are,
    5.1 Run with input command file:
    ```sh
    $ cat tests/data/input4.txt | toy_robot
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
    PLACE X,Y,F:   Place robot at (0<=x<5),(0<=y<5) position facing NORTH, EAST, SOUTH or WEST. Example: PLACE 3,4,WEST
    MOVE       :   Move the toy robot one unit forward in the direction it is currently facing.
    LEFT       :   Rotate the robot 90 degrees left without changing the position of the robot.
    RIGHT      :   Rotate the robot 90 degrees right without changing the position of the robot.
    REPORT     :   Announce the X,Y and F of the robot.
    
    ERROR: First command must be PLACE
    OUTPUT:  0 4 WEST
    ```
    5.2 Run application simulator and provide input command in interpretor mode:
    ```sh
    $ toy_robot

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
    PLACE X,Y,F:   Place robot at (0<=x<5),(0<=y<5) position facing NORTH, EAST, SOUTH or WEST. Example: PLACE 3,4,WEST
    MOVE       :   Move the toy robot one unit forward in the direction it is currently facing.
    LEFT       :   Rotate the robot 90 degrees left without changing the position of the robot.
    RIGHT      :   Rotate the robot 90 degrees right without changing the position of the robot.
REPORT     :   Announce the X,Y and F of the robot.
    ```
    NOTE: Press Ctrl+C to exit the program.
    



