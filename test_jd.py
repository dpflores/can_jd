from can_jd import *
import numpy as np

#CAN
can_jd = CANJD(port, id)    


while True:
    speed = can_jd.get_speed_stimation()
    print(f"velocidad: {speed} m/s")


