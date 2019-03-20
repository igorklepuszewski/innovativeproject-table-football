# Simple demo of reading the MMA8451 orientation every second.
# Author: Tony DiCola
import time
 
import board
import busio
import digitalio
 
import adafruit_mma8451
 

print("This is Accelerometer TEST")

pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("done!")
 
# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
 
# Initialize MMA8451 module.
sensor = adafruit_mma8451.MMA8451(i2c)
# Optionally change the address if it's not the default:
#sensor = adafruit_mma8451.MMA8451(i2c, address=0x1C)
 
# Optionally change the range from its default of +/-4G:
#sensor.range = adafruit_mma8451.RANGE_2G  # +/- 2G
#sensor.range = adafruit_mma8451.RANGE_4G  # +/- 4G (default)
sensor.range = adafruit_mma8451.RANGE_8G  # +/- 8G
 
# Optionally change the data rate from its default of 800hz:
sensor.data_rate = adafruit_mma8451.DATARATE_800HZ  #  800Hz (default)
#sensor.data_rate = adafruit_mma8451.DATARATE_400HZ  #  400Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_200HZ  #  200Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_100HZ  #  100Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_50HZ   #   50Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_12_5HZ # 12.5Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_6_25HZ # 6.25Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_1_56HZ # 1.56Hz
 
# Main loop to print the acceleration and orientation every second.
x1, y1, z1 = sensor.acceleration
print('\tPOMIAR GŁÓWNY \n')
print('x: \t{0: 7.3f} \t\t y: \t{1: 7.3f} \t\t z: \t{2: 7.3f}\n'.format(x1, y1, z1))
while True:
    x, y, z = sensor.acceleration
    x-=x1
    y-=y1
    z-=z1


    print('x: \t{0: 7.3f} \t\t y: \t{1: 7.3f} \t\t z: \t{2: 7.3f}\n'.format(x, y, z))


    time.sleep(.1)

