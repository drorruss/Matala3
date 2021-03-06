from tkinter import Radiobutton
from MyProject.Point import Point
from MyProject.Arena import Arena
from MyProject.Air import *
from MyProject.Robot import Robot
from MyProject.Log import Log
from MyProject.Simulation import Simulation
from MyProject.Message import Message
from MyProject.Global_Parameters import *

readParameters()
Mylog = Log()

#Tests parameter class:
def globalParametersTest():
    print("*********globalParametersTest**************")
    print("BATTARY_CAPACITY", BATTARY_CAPACITY())
    print("TRANSMISSION_RANGE", TRANSMISSION_RANGE())
    print("ROBOTS_NOT_MOVE", ROBOTS_NOT_MOVE())
    print("ROBOTS_MOVE", ROBOTS_MOVE())
    print("ARENA_X", ARENA_X())
    print("ARENA_Y", ARENA_Y())
    print("BLACK_AREA", BLACK_AREA())
    print("GRAY_AREA", GRAY_AREA())
    print("LOG_FILE_DIRECTORY", "|" + LOG_FILE_DIRECTORY() + "|")
    print("WHITE", WHITE()), print("GRAY", GRAY()), print("BLACK", BLACK())
    print("OLDER", OLDER()), print("SAME_AGE", SAME_AGE()), print("YOUNGER", YOUNGER())
    print("UP", UP()), print("LEFT", LEFT()), print("DOWN", DOWN()), print("RIGHT",RIGHT())
    print("INSTANT_SENDING_CHANCE", INSTANT_SENDING_CHANCE())
    print("MAX_NUM_OF_VERSIONS", MAX_NUM_OF_VERSIONS())
    print("MESSAGE_LIFE_TIME", MESSAGE_LIFE_TIME()),print("INFINITY", INFINITY())
    print("MIN_MSG_RANGE", MIN_MSG_RANGE()),print("MAX_MSG_RANGE", MAX_MSG_RANGE())
    print("NO_MSG", NO_MSG()),print("MSG_LIFE_TIME", MSG_LIFE_TIME()),print("MSG_MAX_VERSION", MSG_MAX_VERSION())
    print("MSG_WAIT_TIME", MSG_WAIT_TIME())




#Tests Robot class:
def RobotTest():
    print("**************RobotTest**************")
    Robot.static_arena = Arena()
    Robot.static_air = Air()
    r1 = Robot(0)
    print(r1._id)
    #Env:
    env = r1.getEnv()
    print("getEnv: ",env)
    #move:
    r1.move(UP())
    r1.move(LEFT())
    r1.move(UP())
    r1.move(LEFT())
    print("private location log",end=" :")
    for i in r1._private_location_log: print(i.toString(),end=", ")
    print("\nRandom numbers for direction",end=" :")
    for i in range(0,20): print(r1.getRandomDirection(),end=", ")
    print("\nMessage id's", end=" :")
    for i in range(0, 20): print(r1.creatMessageId(),end=", ")



globalParametersTest()
#RobotTest()

Mylog.close()

