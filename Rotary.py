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


#Dictionairies for Converting from Rotaries to Class

class = {0:1,2:2,4:3,6:4,8:5,10:6,12:"ALLE"}
letters={0:"a",0:"a",2:"b",4:"c",6:"d",8:"e",10:"f",12:"g",14:"h",16:"i",18:"j",20:"k",22:"l",24:"m",26:"ALLE"}

while True:
    clkState1 = GPIO.input(clk1)
    dtState1  = GPIO.input(dt1)
    clkState2 = GPIO.input(clk2)
    dtState2  = GPIO.input(dt2)
    if clkState1 != clkLastState1:
        counter1=(counter1+(2*clkState1!=dtState1)-1)%40
    clkLastState1=clkState1

    #Second Rotary Encoder
    if clkState1 != clkLastState1:
        counter1=(counter1+(2*clkState1!=dtState1)-1)%40
    clkLastState1=clkState1



    sleep(0.01)

