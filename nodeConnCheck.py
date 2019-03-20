import board
import digitalio
import busio

print("This is Accelerometer TEST")

try:
    pin = digitalio.DigitalInOut(board.D4)
    print("Digital IO ok!")

except RuntimeError:
    print("Digital IO error!")

try:
    i2c = busio.I2C(board.SCL, board.SDA)
    print("I2C ok!")

except RuntimeError:
    print("I2C error!")
try:        
    spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
    print("SPI ok!")

except RuntimeError:
    print("SPI error!")

print("done!")