import RPi.GPIO as GPIO
import sleep from time

dt = .1
b1 = 40
b2 = 38
b1State = 1
b1StateOld = 1
b2State = 1
b2StateOld = 1
DC = 99
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(b2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LEDPin , GPIO.OUT)
myPWW = GPIO.PWM(lEDPin, 100)
myPWM.start(DC)
BP = 10
try:
    while True:
        b1State = GPIO.input(b1)
        b2State = GPIO.input(b2)
        if b1StateOld == 0 and b1State ==  1:
            BP = BP-1
            DC = (1.5849)**BP
            print('Dim event')
        if b2StateOld == 0 and b2State == 1:
            BP = BP + 1
            DC = (1.5849)**BP
            print('Bright event')
        if DC > 99:
            DC = 99
        if DC < 0:
            DC = 0
        print(DC)
        myPWM.ChangeDutyCycle(int(DC))
        b1StateOld = b1State
        b2Stateold = b2State
        sleep(dt)


except KeyboardInterrupt :
    myPWM.stop()
    GPIO.cleanup()
    print('GPIO Good to Go')
