from unittest import TestCase
from toy_robot import commands, robot


class CommandTestCase(TestCase):

    def setUp(self):
        self.robot = commands.robot

    def test_place(self):
        command = "PLACE"
        command_args = ["0", "1", "NORTH"]
        commands.execute(command, command_args)
        self.assertEqual(0, self.robot.x)
        self.assertEqual(1, self.robot.y)
        self.assertEqual("NORTH", self.robot.f)

    def test_place_invalid_position(self):
        command = "PLACE"
        command_args = ["0", "1", "NORTH"]
        commands.execute(command, command_args)
        command = "PLACE"
        command_args = ["0", "A", "NORTH"]
        commands.execute(command, command_args)
        self.assertEqual(1, self.robot.y)

    def test_place_invalid_direction(self):
        command = "PLACE"
        command_args = ["2", "3", "WEST"]
        commands.execute(command, command_args)
        command = "PLACE"
        command_args = ["0", "0", "UP"]
        commands.execute(command, command_args)
        self.assertEqual("WEST", self.robot.f)

    def test_place_missing_params(self):
        command = "PLACE"
        command_args = ["4", "1", "SOUTH"]
        commands.execute(command, command_args)
        command = "PLACE"
        command_args = None
        commands.execute(command, command_args)
        self.assertEqual(4, self.robot.x)
        self.assertEqual(1, self.robot.y)
        self.assertEqual("SOUTH", self.robot.f)
 
    def test_move(self):
        command = "PLACE"
        command_args = ["1", "2", "NORTH"]
        commands.execute(command, command_args)
        command = "MOVE"
        command_args = None
        commands.execute(command, command_args)
        self.assertEqual(1, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("NORTH", self.robot.f)

    def test_left(self):
        command = "PLACE"
        command_args = ["4", "1", "NORTH"]
        commands.execute(command, command_args)
        command = "LEFT"
        command_args = None
        commands.execute(command, command_args)
        self.assertEqual(4, self.robot.x)
        self.assertEqual(1, self.robot.y)
        self.assertEqual("WEST", self.robot.f)

    def test_right(self):
        command = "PLACE"
        command_args = ["2", "3", "EAST"]
        commands.execute(command, command_args)
        command = "RIGHT"
        command_args = None
        commands.execute(command, command_args)
        self.assertEqual(2, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("SOUTH", self.robot.f)

    def test_report(self):
        command = "PLACE"
        command_args = ["4", "4", "NORTH"]
        commands.execute(command, command_args)
        command = "REPORT"
        command_args = None
        commands.execute(command, command_args)
