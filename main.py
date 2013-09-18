import time
from Adafruit_BBIO import GPIO


GPIO.setup("USR0", GPIO.OUT)
GPIO.setup("USR1", GPIO.OUT)
GPIO.setup("USR2", GPIO.OUT)
GPIO.setup("USR3", GPIO.OUT)


def blink_all():
    for i in range(0, 10):

        GPIO.output("USR0", GPIO.HIGH)
        GPIO.output("USR1", GPIO.HIGH)
        GPIO.output("USR2", GPIO.HIGH)
        GPIO.output("USR3", GPIO.HIGH)
        time.sleep(2)

        GPIO.output("USR0", GPIO.LOW)
        GPIO.output("USR1", GPIO.LOW)
        GPIO.output("USR2", GPIO.LOW)
        GPIO.output("USR3", GPIO.LOW)
        time.sleep(2)


def main():
    return blink_all()


if __name__ == '__main__':
    main()