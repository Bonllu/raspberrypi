import RPi.GPIO as GPIO
import time
from ADCDevice import * 

ledRedPin = 15
ledGreenPin = 13 
ledBluePin = 11
adc = ADCDevice() 

def setup(): 
    global adc 
    if(adc.detectI2C(0x4b)):
        adc = ADS7830()

    global p_Red, p_Green, p_Blue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledRedPin, GPIO.OUT)
    GPIO.setup(ledGreenPin, GPIO.OUT)
    GPIO.setup(ledBluePin, GPIO.OUT)

    p_Red = GPIO.PWM(ledRedPin, 1000)
    p_Red.start(0)
    p_Green = GPIO.PWM(ledGreenPin, 1000)
    p_Green.start(0)
    p_Blue = GPIO.PWM(ledBluePin, 1000)
    p_Blue.start(0)

def loop():
    while True:
        value_Red = 255-adc.analogRead(0)
        value_Green = 255-adc.analogRead(1)
        value_Blue = 255-adc.analogRead(2) 
        p_Red.ChangeDutyCycle(value_Red*100/255)
        p_Green.ChangeDutyCycle(value_Green*100/255)
        p_Blue.ChangeDutyCycle(value_Blue*100/255)
        print('ADC Value value_Red: %d, \tvlue_Green: %d, \tvalue_Blue: %d' %(value_Red, value_Green, value_Blue))
        time.sleep(0.01) 

def destroy():
    adc.close()
    GPIO.cleanup() 

if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
   
