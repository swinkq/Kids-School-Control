from gpiozero import LED
from time import sleep

led = LED(26)

while True:
    led.on()
    sleep(3)
    led.off()
    led.cleanup()
   # sleep(1)

