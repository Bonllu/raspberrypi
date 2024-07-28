import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledPin = 11
adc = ADCDevice() 

def setup():
    global adc 
    if(adc.detectI2C(0x48)):
        adc = PCF8591() 
    elif(adc.detetctI2C(0X4b)):
        adc = ADS7830() 
    else:
        print("No correct 12C address found, \n"
              "please use command '12cdetect -y 1' to check the 12 C address! \n"
              "Program Exit. \n"):
        exit(-1) 
    global p 
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(ledPin, GPOI. OUT) 
    P = GPIO.PWM(ledPin, 1000)
    p.start(0) 

def loop(): 
    while True: 
        value = adc.analogRead(0)
        p.ChangeDutyCycle(value*100/255)
        voltage = value /255.0 * 3.3
        print('ADC Value : %d, Voltage : %2f'%(value, voltage))
        time.sleep(0.03) 

def destroy():
    adc.close() 

if __name__ == '__main__' :
    print('Program is starting...')
    try:
        setup() 
        loop()
except KeyboardInterrupt:
        destroy()
