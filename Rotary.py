from time import sleep
from RPi import GPIO


clk1=17
dt1=18
clk2=27
dt2=22

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


counter1=0
counter2=0
clkLastState1=GPIO.input(clk1)
clkLastState2=GPIO.input(clk2)
