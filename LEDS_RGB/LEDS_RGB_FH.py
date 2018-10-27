class LEDS_RGB_FH:

    LED1 = 0
    LED2 = 1
    __LEDS_GPIO = [[1, 0, 2], [4, 3, 15]]
    
    def __init__(self, pwm):
        self.__pwm = pwm


    def setColor(self, led, color):
        
        for i in range(len(self.__LEDS_GPIO[led])):
            self.__pwm.set_pwm(self.__LEDS_GPIO[led][i], 0, color[i])

    def off(self, led):
        
        self.setColor(led, [0, 0, 0])
