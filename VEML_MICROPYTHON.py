# -*- coding: utf-8 -*-
'''!
  @file DFRobot_VEML6075_demo.py
  @brief Test normal pour le VEML6075
  @n     L'indice UVA, l'indice UVB et l'indice UV seront imprimés sur la console
  @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     La licence MIT (MIT)
  @maintainer [Fary](feng.yang@dfrobot.com)
  @version  V1.0
  @date  2021-10-18
  @url https://github.com/DFRobot/DFRobot_VEML6075
'''

import time
from DFRobot_VEML6075 import DFRobot_VEML6075

if __name__ == '__main__':
    VEML6075 = DFRobot_VEML6075(1, 0x10)  # utilise le bus i2c 1, adresse du module : 0x10

    while not VEML6075.begin():
        print("Échec de l'initialisation de VEML6075")
        time.sleep(2)
    print("Initialisation de VEML6075 réussie")
    
    while True:
        Uva = VEML6075._read_reg(VEML6075.UVA, 2)
        Uva = Uva[0] | (Uva[1] << 8)
        Uvb = VEML6075._read_reg(VEML6075.UVB, 2)
        Uvb = Uvb[0] | (Uvb[1] << 8)
        
        Uva_responsivity_list = VEML6075.uva_responsivity_list
        Uvb_responsivity_list = VEML6075.Uvb_responsivity_list
        Uva = Uva * (1.0 / 1.0) * Uva_responsivity_list[VEML6075._UV_IT]
        Uvb = Uvb * (1.0 / 1.0) * Uvb_responsivity_list[VEML6075._UV_IT]
        
        Uvi = (Uva + Uvb) / 2
        
        print("")
        print("======== start print ========")
        print("UVA:     %.2f" % (Uva))
        print("UVB:     %.2f" % (Uvb))
        print("UVI:     %.2f" % (Uvi))
        print("mw/cm^2: %.2f" % (VEML6075.uvi2mwpcm2(Uvi)))
        print("======== end print =========")
        time.sleep(1)
