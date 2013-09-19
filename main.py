import time
from Adafruit_BBIO import GPIO


LEDS = {
    "USR0": 53,
    "USR1": 54,
    "USR2": 55,
    "USR3": 56
}

GPIO.setup(LEDS["USR0"], GPIO.OUT)
GPIO.setup(LEDS["USR1"], GPIO.OUT)
GPIO.setup(LEDS["USR2"], GPIO.OUT)
GPIO.setup(LEDS["USR3"], GPIO.OUT)


def blink_all():
    for i in range(0, 10):

        GPIO.output(LEDS["USR0"], GPIO.HIGH)
        GPIO.output(LEDS["USR1"], GPIO.HIGH)
        GPIO.output(LEDS["USR2"], GPIO.HIGH)
        GPIO.output(LEDS["USR3"], GPIO.HIGH)
        print "LEDs ON"
        time.sleep(2)

        GPIO.output(LEDS["USR0"], GPIO.LOW)
        GPIO.output(LEDS["USR1"], GPIO.LOW)
        GPIO.output(LEDS["USR2"], GPIO.LOW)
        GPIO.output(LEDS["USR3"], GPIO.LOW)
        print "LEDs OFF"
        time.sleep(2)


def main():
    return blink_all()


if __name__ == '__main__':
    main()