import time
from Adafruit_BBIO import GPIO


GPIO.setup("USR_0", GPIO.OUT)
GPIO.setup("USR_1", GPIO.OUT)
GPIO.setup("USR_2", GPIO.OUT)
GPIO.setup("USR_3", GPIO.OUT)


def blink_all():
    for i in range(0, 10):

        GPIO.output("USR_0", GPIO.HIGH)
        GPIO.output("USR_1", GPIO.HIGH)
        GPIO.output("USR_2", GPIO.HIGH)
        GPIO.output("USR_3", GPIO.HIGH)
        print "LEDs ON"
        time.sleep(2)

        GPIO.output("USR_0", GPIO.LOW)
        GPIO.output("USR_1", GPIO.LOW)
        GPIO.output("USR_2", GPIO.LOW)
        GPIO.output("USR_3", GPIO.LOW)
        print "LEDs OFF"
        time.sleep(2)


def main():
    return blink_all()


if __name__ == '__main__':
    main()