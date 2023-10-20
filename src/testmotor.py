import RPi.GPIO as GPIO
import time

# Set pin numbering mode (choose either GPIO.BOARD or GPIO.BCM)
GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

# Define pin numbers
in1 = 14
in2 = 15
enB = 18
in1a = 4
in2a = 3
enBa = 2

# Initialize GPIO
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

# Initialize GPIO
GPIO.setup(in1a, GPIO.OUT)
GPIO.setup(in2a, GPIO.OUT)
GPIO.setup(enBa, GPIO.OUT)

# Initialize PWM for enB
pwm = GPIO.PWM(enB, 100)  # 100 Hz frequency
pwm.start(0)  # Starts with 0% duty cycle (stopped)

pwma = GPIO.PWM(enBa, 100)  # 100 Hz frequency
pwma.start(0)  # Starts with 0% duty cycle (stopped)

# Define functions to control the motor

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    GPIO.output(in1a, GPIO.LOW)
    GPIO.output(in2a, GPIO.LOW)
    pwma.ChangeDutyCycle(0)

def forward(speed):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def backward(speed):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)


def right(speed):
    GPIO.output(in1a, GPIO.HIGH)
    GPIO.output(in2a, GPIO.LOW)
    pwma.ChangeDutyCycle(speed)

def left(speed):
    GPIO.output(in1a, GPIO.LOW)
    GPIO.output(in2a, GPIO.HIGH)
    pwma.ChangeDutyCycle(speed)
# Example usage

try:
    forward(40)  # Move forward at 50% speed
    time.sleep(3) 

    stop()  # Stop the motor
    GPIO.cleanup()  # Clean up GPIO on program exit
finally:
    GPIO.cleanup()  # Clean up GPIO on program exit
