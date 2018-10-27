import Adafruit_PCA9685 as PWM
import LEDS_RGB_FH as LEDS
import time

def main():
    
    pwm = PWM.PCA9685(0x70)
    pwm.set_pwm_freq(60)

    leds = LEDS.LEDS_RGB_FH(pwm)

    while(True):

        leds.setColor(leds.LED1, [255, 0, 0])
        leds.off(leds.LED2)
        time.sleep(.200)
        leds.setColor(leds.LED2, [0, 0, 255])
        leds.off(leds.LED1)
        time.sleep(.200)

main()
    
