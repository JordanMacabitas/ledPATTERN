import serial
import time

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)

print("Commands: pattern1, pattern2, pattern3, pattern4, pattern5, off, exit")

command = input("Enter command: ")

if command == "EXIT":
    print("Program stopped.")
else:
    arduino.write((command + "\n").encode())
    print("Command sent:", command)
    time.sleep(1)