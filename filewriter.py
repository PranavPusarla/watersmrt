##############
## Script listens to serial port and writes contents into a file

import serial  # sudo pip install pyserial should work
from datetime import datetime

serial_port = '/dev/cu.usbmodem1411';
baud_rate = 9600;  #In arduino, Serial.begin(baud_rate)
write_to_file_path = "week.txt";

output_file = open(write_to_file_path, "w+");
ser = serial.Serial(serial_port, baud_rate)
output_file.write(str(datetime.now().timestamp()) + "\n")
count = 0
while True:
    count += 1;
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    print(line);
    if (count % 3 == 0):
        output_file.write(line + "\n");
    else:
        output_file.write(line);
