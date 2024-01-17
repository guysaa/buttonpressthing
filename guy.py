import serial
import os

# Set up the serial connection
ser = serial.Serial('COM3', 9600)

# Read input from the serial port
while True:
    input_str = ser.readline().decode().strip()
    if input_str == '3':
        os.startfile('sun.jpg')
    elif input_str == '2':
        os.startfile('earth.jpg')
