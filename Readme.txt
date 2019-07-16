--Project descript--
Project uses Motion sensor, temperature sensor and light sensor
- Motion sensor is used to detect human to turn on and turn off the light in the building
- Temperature sensor is used to measure temperate to turn on and turn off the fan, also depending on the human detection condition.
- Light sensor is used to measure the luminance, to turn on and turn of the light in the front of building. emergency exit.
- Also, camera is used to capture the image of the people who press the door bell to send to security guard.
- all sensor data and energy consumption will be stored in the database

--Project implementation---
sensor is used to communicate with environment and send data to API planner through the message queue MQTT. An encoder function is used
to provide correct init value for AI planner PDDL. AI planner will output the actions which need to be done. These information will be
sent to Actuator through the message queue MQTT to control plugwise turn on and turn off the device. 
We have only two plugwise so the turn the light on the front of building and camera will be demonstrated on breadboard.

--- Run the programm---
run the start.py then it wil call and execute the Mainprogram
