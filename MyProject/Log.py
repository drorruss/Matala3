from MyProject.Global_Parameters import *


class Log:
    def __init__(self):
        global file

        file = open(LOG_FILE_DIRECTORY(), "w")

    def addLine(line):
        file.write(line +"\n")

    def close(self):
        file.close()
