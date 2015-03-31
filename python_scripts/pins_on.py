#!/usr/bin/env python
import sys

galileo_path = "/opt/pyGalileo/"
if galileo_path not in sys.path:
    sys.path.append(galileo_path)

from pyGalileo import *

'''/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 '''

#// the setup routine runs once when you press reset:
def pin_off(led_int):
    pinMode(led_int, OUTPUT)
    digitalWrite(led_int, LOW)

def pin_on(led_int):
    pinMode(led_int, OUTPUT)
    digitalWrite(led_int, HIGH)

if __name__ == "__main__":
    for pin in range(1,14):
        pin_on( pin )
