# Leds RGB Red Hat

Como podemos ver en la imagen, cada LED RGB de la Red Hat está conectado a tres salidas PWM, una para cada color.

<p align="center">
    <img src="https://github.com/gunhack/Raspberry_FezHat/blob/master/img/LED_RGB/LED_RGB_1.PNG?raw=true" alt="Test I2C" height="300"/>
</p>

---

## Clase LEDS_RGB_FH

En la librería vemos la clase ***LEDS_RGB_FH*** la cual encapsula los dos leds RGB que tiene la placa.

Las constantes:

``` python
    LED1 = 0
    LED2 = 1
```
permiten al usuario seleccionar facilmente que led quieren encender.

El arreglo:

``` python
__LEDS_GPIO = [[1, 0, 2], [4, 3, 15]]
```
son los pines del PWM al que está conectado cada entrada del LED RGB (Red, Green, Blue) respectivamente.

Podemos observar el código del constructor:
``` python
def __init__(self, pwm):
    self.__pwm = pwm
```
el cuál recibe como parámetro un objeto PWM y lo copia en su variable de clase ***__pwm***.

La función setColor es la que hace toda la mágia, la cual recibe como parámetros el LED que se quiere encender, y un arreglo el cual tiene los valores R, G, B respectivamente (R, G, B <= 255).
``` python
def setColor(self, led, color):
        
        for i in range(3):
            self.__pwm.set_pwm(self.__LEDS_GPIO[led][i], 0, color[i])
```
---

## Prueba

En el archivo [test.py](https://github.com/gunhack/Raspberry_FezHat/blob/master/LEDS_RGB/test.py) podemos observar como importamos la librería ***Adafruit_PCA9685***

``` python
import Adafruit_PCA9685 as PWM
```
La cual contiene la clase PWM la cuál nos permite sacar valores analógicos a travez del PWM integrado en la Red Hat.

En la función ***main*** creamos el objeto ***pwm*** al cual al inicializarlo se le manda la dirección en donde se encuentra el PWM. En mi caso es la ***0x70*** la cual se obtiene verificando nuestras salidas IC2 en una terminal.
<p align="center">
    <img src="https://github.com/gunhack/Raspberry_FezHat/blob/master/img/general/testI2C.PNG?raw=true" alt="Test I2C" height="400"/>
</p>

``` python
pwm = PWM.PCA9685(0x70)
pwm.set_pwm_freq(60)
```
También se le coloca la frecuencia con la que se desea trabajar, en mi caso coloqué **60**.

La parte principal del programa se encuentra en el ciclo ***while***:

``` python
 while(True):
    leds.setColor(leds.LED1, [255, 0, 0])
    leds.off(leds.LED2)
    time.sleep(.200)
    leds.setColor(leds.LED2, [0, 0, 255])
    leds.off(leds.LED1)
    time.sleep(.200)
```
Aquí podemos observar como encendemos el color rojo en el LED 1, apagamos el LED 2, esperamos ***.2 segundos***, encendemos el LED 2 con el color azul, apagamos el LED 1 y volvemos a esperar .2 segundos. Como una torreta de policía xD
