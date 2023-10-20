<div align="center">

# Autonomous-Computer-Vision-Car

</div>

## Overview
The main objective of this project was to create a simple robot that using computer vison could follow another robot. This project utilized many different components such as a Raspberry pi 4, L298N motor driver, USB cam, Motors and Battery packs as well as power regulators. This code is made to run on a Raspberry pi 4, and it uses a pre-trained model that I trained in a [previous repositry.](https://github.com/AydenBravender/Spyder_RC_Car_TF_Model) Inside the src file there are 2 main python scripts, server.py, and computer_vision_transmitter.py. The latter one opens up a usb webcam on your raspberry pi, and detects the robot ahead of it. This data is then anaylazed to be sent via socket to server.py. Here, the script calculates the centroid of the object in respect to itself, and moves left or right depending on what the data indicates.

## Using Code

First clone this repo: https://github.com/AydenBravender/Autonomous-Computer-Vision-Car.git
by running ```git clone https://github.com/AydenBravender/Autonomous-Computer-Vision-Car.git```

Next move into the directory called src by running ```cd Autonomous-Computer-Vision-Car/src```

You can use either [my model](https://github.com/AydenBravender/Spyder_RC_Car_TF_Model) trained on a certain type of RC cars, or your own. If you chose to use your own, make sure to replace where ever I say "custom_model_lite/" with your model name. (In the trackrobot.sh script) 

Move either model into the src directory.
In server.py as well as computer_vision_transmitter.py, it has a line that says ```server_socket.bind(('127.0.0.1', 11312))``` Make sure to replace this with your computers information.

I like to start with running ```sudo apt-get update``` and ```sudo apt-get upgrade```

Install virtualenv: ```pip3 install virtualenv```
Now we can create a virtual enviroment by running ```python3 -m virtualenv TFlite1-env```
Initilize the enviroment by running ```source TFlite1-env/bin/activate```  
Finally run ```pip install -r requirements.txt``` this may take a while.

Now you have 2 choices. 

### Choice 1
You can open up 2 terminals and navigate to the src diretory, and initilize the enviroment for both of them. 
Then run in one ```python3 server.py``` and in the other ```python3 computer_vision_transmitter.py --modeldir=custom_model_lite/```
This should run the car! If using your own model make sure to replace ```custom_model_lite/``` with your own model directory.

### Choice 2
make the shell script ```trackrobot.sh``` exectuble by ```chmod +x trackrobot.sh```
Then run it ```./trackrobot.sh```
If you are using your own model, go into the shell script and replace the current model name "custom_model_lite/" with your model name
Give it a few seconds. It might give an OS error, but you can ignore it from now.

