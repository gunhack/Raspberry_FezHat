# Raspberry & Fez Hat

<p align="center">
    <img src="https://www.raspberrypi.org/app/uploads/2018/03/RPi-Logo-Reg-SCREEN.png" alt="Rapsberry logo"  height="100"/>
</p>


## Introducción

Éste repositorio fue creado para la instalación y uso de la placa [Fez Hat](https://www.generationrobots.com/en/402284-fez-hat.html) la cual viene ensamblada y pre-programada para el fácil uso de sus componentes.

La placa es excelente para quienes empiezan en el mundo de la programacíon de la Raspberry.

----

## Contenido

1) [Fez Hat](https://github.com/gunhack/RaspberryFezHat#1-fez-hat)
    * 1.1 [Especificaciones](https://github.com/gunhack/RaspberryFezHat#11-especificaciones)
2) [Instalación](https://github.com/gunhack/RaspberryFezHat#2-instalaci%C3%B3n)
    * 2.1 [Raspbian](https://github.com/gunhack/RaspberryFezHat#21-raspbian)
    * 2.2 [Antes de instalar las librerías](https://github.com/gunhack/RaspberryFezHat#22-antes-de-instalar-las-librer%C3%ADas)
    * 2.3 [Adafruit Pi Code](https://github.com/gunhack/RaspberryFezHat#23-adafruit-pi-code)
    * 2.4 [Configurando I2C](https://github.com/gunhack/RaspberryFezHat#24-configurando-i2c)
        * 2.4.1 [Configurando el soporte del kernel para I2C](https://github.com/gunhack/RaspberryFezHat#241-configurando-el-soporte-del-kernel)
        * 2.4.2 [2.6 Probando el I2C](https://github.com/gunhack/RaspberryFezHat#242-probando-el-i2c)
    * 2.5 [Configuring SPI (Opcional)](https://github.com/gunhack/RaspberryFezHat#25-configuring-spi-opcional)
        * 2.5.1 [Probando el SPI](https://github.com/gunhack/RaspberryFezHat#251-probando-el-spi)
3) [Lista de Sensores](https://github.com/gunhack/RaspberryFezHat#3-lista-de-sensores)

---
## 1. Fez Hat

Con la Fez HAt tienes todo lo que neccesitas para construir pequeños robots o gadgets en la Raspberry Pi. Ésta shield ya tiene terminales para servomotores y motoreductores y tambien te da la posibilidad de añadir otros módulos de tu preferencia para mejorar tu creación.

<p align="center">
    <img id="bigpic" itemprop="image" src="https://static.generation-robots.com/5908-large_default/fez-hat.jpg" title="FEZ HAT" alt="FEZ HAT" height="200">
</p>


### 1.1 Especificaciones

* Chips PWM y una entrada análoga integrada
* 2 Drivers de motoreductores, para la construccion de pequeños robots
* Terminales para conectar sin soldar los motoreductores
* 2 Conecciones para serovomotores
* 2 LED RGB
* 1 LED rojo
* 1 Sensor de temperatura
* 1 Acelerómetro
* 1 Sensor de Luz
* 2 Botones
* 1 Terminal con 2 conectores análogos, 2 conectores digitales de I/O, 2 conectores PWM y 1 conector de corrriente
* Pines hembra con SPI, I2C, 3 análogos, 3 PWM
* Entrada de energía dedicada para los servo y motoreductores

<p align="center">
    <a class="catalogue" title="FEZ HAT by Gadgeteer - technical schematic" href="https://www.generationrobots.com/media/FEZ_HAT_SCHEMA.pdf" target="_blank"><img src="http://static.generation-robots.com/img/cms/fez-hat-schema.jpg" alt="FEZ HAT by Gadgeteer - technical schematic" width="480"></a>
</p>

---

## 2. Instalación


### 2.1 Raspbian

Es necesario tener la última versión de [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) en la Rapsberry

<p align="center">
    <a href="http://www.youtube.com/watch?feature=Zo9vAStziwE&v=Zo9vAStziwE" target="_blank"><img src="http://img.youtube.com/vi/Zo9vAStziwE/0.jpg" alt="Cómo instalar Raspbian"/></a>
</p>

### 2.2 Antes de instalar las librerías

Una vez teniendo instalado Raspbian es necesario descargar algunas librerías.

Antes de instalar algo, usa el siguiente comando para asegurar que tu distribución esté en su versión actualizada. No importa el directorio donde estés.

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get dist-upgrade

Este proceso podría tardar, especialmente si es la primera vez que lo haces.
Cuando termine tendrás que instalar Git si aun no lo tienes.

    sudo apt-get install git

También hay que comprobar que tenemos intaladas las librerías Rpi.GPIO para eso utilizamos el comando:

    sudo apt-get install python-rpi.gpio python3-rpi.gpio


### 2.3 Adafruit Pi Code

Ahora si podemos instalar las liberías necesarias, en este caso son algunas de las que Adafruit nos proporciona, el repositorio original lo encontrás [aquí.](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code)

La primera es [Adafruit Python GPIO Library](https://github.com/adafruit/Adafruit_Python_GPIO)

Para instalarla hay que usar los siguientes comandos:

    git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
    cd Adafruit_Python_GPIO
    sudo python setup.py install

Y la segunda es [Adafruit Python PCA9685](https://github.com/adafruit/Adafruit_Python_PCA9685)

Los comados para instalarla (similares a la primera):

    git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
    cd Adafruit_Python_PCA9685
    sudo python setup.py install

Cabe mencionar que si estás utilizando Python 3.x al momento de ejecutar el comando:

    sudo python setup.py install

hay que agregarle un "3" para instalarlo en la versión 3.x

    sudo python3 setup.py install

### 2.4 Configurando I2C

I2C es un estándar muy comunmente utilizado para permitir la comunicación de un chip a otro. Así que desde que la Raspbrry puede "hablar" I2C, podemos conectar una gran variedad de módulos y chips I2C. 

El bus I2C nos permite conectar múltiples dispositivos a tu Raspberry Pi, con una dirección (registro) única, que a menudo se puede configurar cambiando la configuración del puente en el módulo. Es muy útil poder ver en que dirección están conectados los dispoositivos en la Raspberry como manera de estar seguro de que está funcionando.

Para hacer esto necesitamos ejecutar los siguientes comandos para instalar las herramientas de I2C.

    sudo apt-get install python-smbus python3-smbus python-dev python3-dev
    sudo apt-get install -y i2c-tools

#### 2.4.1 Configurando el soporte del kernel

Ejecuta el siguiente comando y sigue las capturas para instalar el soporte de I2C para el ARM core y el kernel de Linux:

    sudo raspi-config

* Selecciona **Interfacing Options**
<p align="center">
   <img src="https://github.com/gunhack/Raspberry_FezHat/blob/master/img/general/I2C_1.PNG?raw=true" alt="Configurar I2C"/>
</p>

* Después **I2C**
<p align="center">
   <img src="https://github.com/gunhack/Raspberry_FezHat/blob/master/img/general/I2C_2.PNG?raw=true" alt="Configurar I2C"/>
</p>

* Cuado pregunte que si lo queremos habilitar, seleccionamos **YES**
<p align="center">
   <img src="https://github.com/gunhack/Raspberry_FezHat/blob/master/img/general/I2C_3.PNG?raw=true" alt="Configurar I2C"/>
</p>

* Aparecerá la ventana de confirmación

<p align="center">
   <img src="https://github.com/gunhack/Raspberry_FezHat/blob/master/img/general/I2C_4.PNG?raw=true" alt="Configurar I2C"/>
</p>

* Una vez que esté listo, reinicia.

```
sudo reboot
```

#### 2.4.2 Probando el I2C

Prueba el siguiente comando para ver todos los dispositivos conectados (Conecta primero la Red Hat)

    sudo i2cdetect -y 1

---

### 2.5 Configurando SPI (Opcional)

De nuevo ejecutamos el comando:

     sudo raspi-config

* Seleccionamos **Interfacing Options**

* Sleccionamos **SPI**

* Cuado pregunte que si lo queremos habilitar, seleccionamos **YES**

* Reiniciamos

#### 2.5.1 Probando el SPI

Ejecutando el siguiente comando:

    ls -l /dev/spidev*

deberías poder ver los dispoitivos SPI

---
## 3. Lista de Sensores

Una vez concuidos todos los pasos anteriores puedes probar las librerías que hice para cada uno de los módulos que tiene la Red Hat.

### 3.1 Básicos
1) [Leds RGB y PWM](https://github.com/gunhack/Raspberry_FezHat/tree/master/LEDS_RGB)