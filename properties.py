import numpy as np
import CoolProp as CP
import pytemperature as temp
import psychrolib
from CoolProp.CoolProp import PropsSI
psychrolib.SetUnitSystem(psychrolib.SI)
Density=CP.HumidAirProp.HAPropsSI('D','T',300,'P',101325,'R',0.1)
WBT = psychrolib.GetTWetBulbFromHumRatio(35,0.007,101325)

Tdp =psychrolib.GetTDewPointFromRelHum(35,0.4)
print(WBT,Tdp)