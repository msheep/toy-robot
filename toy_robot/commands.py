from toy_robot import robot

robot = robot.Robot()


def execute(cmd, cmd_args):
    try:
        if cmd == "PLACE":
            robot.place(cmd_args[0], cmd_args[1], cmd_args[2])
        elif cmd == "MOVE":
            robot.move()
        elif cmd == "LEFT":
            robot.turn_left()
        elif cmd == "RIGHT":
            robot.turn_right()
        elif cmd == "REPORT":
            robot.report()
        else:
            print("ERROR: Invalid command: ", cmd)
    except (IndexError, TypeError):
        print("ERROR: Invalid command args: ", cmd_args)
