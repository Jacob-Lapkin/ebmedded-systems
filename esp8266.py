from machine import Pin
import utime
import urequests as requests
import network
print("2")
# connect to ultrasonic sensor
trigger = Pin(1, Pin.OUT)
echo = Pin(3, Pin.IN)
# connect to onboard led light
led = Pin(16, Pin.OUT)


# connect to wifi
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Jakeandjubes', 'redhotchilipeppers')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


# function for ultrasonic sensor
def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
   return distance


# connect to wifi
do_connect()

print("3")

while True:
    while ultra() > 20:
        led.value(0)
        utime.sleep(.2)
        led.value(1)
        utime.sleep(.2)
    while ultra() <= 20:
        res = requests.get(url='https://api.agify.io/?name=meelad').json()
        print(res.get("age"))
        utime.sleep(10)

    