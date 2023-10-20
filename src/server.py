import socket
import ast
import RPi.GPIO as GPIO
import time

steer_1 = 4 # pin 7
steer_2 = 3 # pin 5
enA = 2 # pin 3

drive_1 = 14 # pin 36
drive_2 = 15 # pin 38
enB = 18 # pin 40

GPIO.setmode(GPIO.BCM)

pins = [drive_1,drive_2,enA,steer_1,steer_2,enB]

for element in pins:
	GPIO.setup(element,GPIO.OUT) # to set up all GPIO pins
	if element != enA or enB:
		GPIO.output(element,GPIO.LOW) # to set all drive pins low

steer=GPIO.PWM(enA,1000) # '1000' hertz duty cycle
drive=GPIO.PWM(enB,1000)
drive.start(0) # starting the drive motor at a pre-set duty cycle
steer.start(100)

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 11312))
server_socket.listen(1)

data = []
while True:
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:
        received_data = client_socket.recv(1024).decode()
        if not received_data:
            break
        data.append(received_data)
        print(f"Data received: {data}")
        
        GPIO.output(drive_1, GPIO.HIGH)
        GPIO.output(drive_2, GPIO.LOW)
        drive.ChangeDutyCycle(80)

        try:
            parsed_list = ast.literal_eval(data[-1])  # Parse the last received data as a list
            if isinstance(parsed_list, list):
                print(parsed_list)
                areax = parsed_list[3] - parsed_list[2]
                areay = parsed_list[1] - parsed_list[0]
                area = areax * areay
                sumx = parsed_list[2] + parsed_list[3]
                centroid = sumx/2
                if centroid > 625:
                    print("RIGHT")
                    GPIO.output(steer_1,GPIO.HIGH)
                    GPIO.output(steer_2,GPIO.LOW)
                    time.sleep(0.2)
                if centroid < 575:
                    print("LEFT")
                    GPIO.output(steer_1,GPIO.LOW)
                    GPIO.output(steer_2,GPIO.HIGH)
                    time.sleep(0.2)
        except (ValueError, SyntaxError):
            print("Invalid data format")

    print(f"Connection closed")
    client_socket.close()

server_socket.close()
