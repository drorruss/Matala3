

from MyProject.Log import Log
from MyProject.Simulation import Simulation
from MyProject.Global_Parameters import *




readParameters() # reading file Parameters from Parameters txt
Mylog = Log()



s = Simulation() # runnung the simulation
s.showGUI()

Mylog.close()



