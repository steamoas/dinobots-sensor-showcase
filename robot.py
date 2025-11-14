from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Color, Direction, Port


large_fanta = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rural_large_frys_and_10_chicken_nuggets_at_Mcdonalds = Motor(Port.F, Direction.CLOCKWISE)
drive = DriveBase(large_fanta, rural_large_frys_and_10_chicken_nuggets_at_Mcdonalds, 56, 88)
drive.use_gyro(True)
drive.curve(150, -180)
