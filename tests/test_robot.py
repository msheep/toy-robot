from unittest import TestCase
from toy_robot import robot


class RobotTestCase(TestCase):

    def setUp(self):
        self.robot = robot.Robot()

    def test_place(self):
        self.robot.place("3", "0", "WEST")
        self.assertEqual(3, self.robot.x)
        self.assertEqual(0, self.robot.y)
        self.assertEqual("WEST", self.robot.f)

    def test_place_out_of_upper_bounds(self):
        # Valid placement
        self.robot.place("1", "0", "NORTH")
        # Invalid placement should be ignored
        self.robot.place("5", "4", "NORTH")
        self.assertEqual(1, self.robot.x)
        self.assertEqual(0, self.robot.y)
        self.assertEqual("NORTH", self.robot.f)

    def test_place_out_of_lower_bounds(self):
        # Valid placement
        self.robot.place("1", "3", "WEST")
        # Invalid placement should be ignored
        self.robot.place("-1", "0", "NORTH")
        self.assertEqual(1, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("WEST", self.robot.f)

    def test_move(self):
        self.robot.place("2", "3", "NORTH")
        self.robot.move()
        self.assertEqual(2, self.robot.x)
        self.assertEqual(4, self.robot.y)
        self.assertEqual("NORTH", self.robot.f)

    def test_move_out_of_upper_bounds(self):
        self.robot.place("4", "3", "EAST")
        self.robot.move()
        self.assertEqual(4, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("EAST", self.robot.f)

    def test_move_out_of_lower_bounds(self):
        self.robot.place("4", "0", "SOUTH")
        self.robot.move()
        self.assertEqual(4, self.robot.x)
        self.assertEqual(0, self.robot.y)
        self.assertEqual("SOUTH", self.robot.f)

    def test_left(self):
        self.robot.place("2", "3", "SOUTH")
  
        self.robot.turn_left()
        self.assertEqual(2, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("EAST", self.robot.f)

        self.robot.turn_left()
        self.assertEqual(2, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("NORTH", self.robot.f)

        self.robot.turn_left()
        self.assertEqual(2, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("WEST", self.robot.f)

        self.robot.turn_left()
        self.assertEqual(2, self.robot.x)
        self.assertEqual(3, self.robot.y)
        self.assertEqual("SOUTH", self.robot.f)

    def test_right(self):
        self.robot.place("3", "4", "SOUTH")

        self.robot.turn_right()
        self.assertEqual(3, self.robot.x)
        self.assertEqual(4, self.robot.y)
        self.assertEqual("WEST", self.robot.f)

        self.robot.turn_right()
        self.assertEqual(3, self.robot.x)
        self.assertEqual(4, self.robot.y)
        self.assertEqual("NORTH", self.robot.f)

        self.robot.turn_right()
        self.assertEqual(3, self.robot.x)
        self.assertEqual(4, self.robot.y)
        self.assertEqual("EAST", self.robot.f)

        self.robot.turn_right()
        self.assertEqual(3, self.robot.x)
        self.assertEqual(4, self.robot.y)
        self.assertEqual("SOUTH", self.robot.f)

    def test_report(self):
        self.robot.place(2, 4, "NORTH")
        self.robot.report()
