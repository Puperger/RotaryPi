from time import sleep
from RPi import GPIO
from gpiozero import Button

clk1=17
dt1=18
clk2=27
dt2=22
sw1=Button(23)
sw2=Button(24)

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

classes={0:1,2:2,4:3,6:4,8:5,10:6,12:"ALLE"}
letters={0:"a",0:"a",2:"b",4:"c",6:"d",8:"e",10:"f",12:"g",14:"h",16:"i",18:"j",20:"k",22:"l",24:"m",26:"ALLE"}

while True:
    clkState1 = GPIO.input(clk1)
    dtState1  = GPIO.input(dt1)
    clkState2 = GPIO.input(clk2)
    dtState2  = GPIO.input(dt2)

    if clkState1 != clkLastState1:
        if clkState1!=dtState1:
            counter1+=1
        else:
            counter1-=1
    clkLastState1=clkState1
    

    #Second Rotary Encoder
    if clkState2 != clkLastState2:
        if clkState2!=dtState2:
            counter2+=1
        else:
            counter2-=1
    clkLastState2=clkState2
    
    if sw1.is_pressed and sw2.is_pressed:
        for i in range(500):
            if not (sw1.is_pressed and sw2.is_pressed):
                break
            sleep(0.01)
        else:
            print("RESET")
    
    elif sw1.is_pressed:
        print("Sending...")
        for i in range(500):
            if sw2.is_pressed:
                print("CANCELED")
                break
        else:
            print("Sent Successfully")

    sleep(0.001)


