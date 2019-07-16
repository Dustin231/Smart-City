#!/usr/bin/python

import openzwave
from openzwave.option import ZWaveOption
from openzwave.network import ZWaveNetwork
from openzwave.controller import ZWaveController
from openzwave.node import ZWaveNode
from openzwave.value import ZWaveValue
from openzwave.scene import ZWaveScene
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time
from time import sleep
import os
import sqlite3
from sqlite3 import Error
import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output  


options  = ZWaveOption("/dev/ttyACM0",config_path='/home/pi/python-openzwave/openzwave/config',user_path=".")
options.set_console_output(False)
options.lock()

network = ZWaveNetwork(options, log =None)
network.start()

global m, t, s, k, id, temperature, sensor, luminance, datetime, doorbell

while network.state != network.STATE_READY:
	sleep(1)

print ("Network Ready")

while True:
	sleep(2)
	for node in network.nodes:
		for sensor in network.nodes[node].get_sensors().items():
			x=sensor[1].label
			y=sensor[1].data
			z = list()
			print(x)
			print(y)

			if(x == "Sensor"):
				Detec = y
				if Detec == 1:
					t = 1
				else:
					t = 0
				MQTT_SERVER = "192.168.0.108"
				MQTT_PATH = "test_channel"
				publish.single(MQTT_PATH, t, hostname=MQTT_SERVER)


			if(x == "Temperature"):
				temp = y
				if temp > 20:
					m = 1
				else:
					m = 0

				MQTT_SERVER = "192.168.0.108"
				MQTT_PATH = "test_channel"
				publish.single(MQTT_PATH, m, hostname=MQTT_SERVER)

			if(x == "Luminance"):
				Lum = y
				if Lum > 2:
					s = 1
				else:
					s = 0
				MQTT_SERVER = "192.168.0.108"
				MQTT_PATH = "test_channel"
				publish.single(MQTT_PATH, s, hostname=MQTT_SERVER)
		
		
	class encoder:
		def __init__(self, detection, temperature, light, button):
			self.detection = detection
			self.temperate = temperature
			self.light = light
			self.button = button

		def encoder_function (self):
			with open('FF-v2.3/ProblemFinal.pddl', 'r') as file:
				# read a list of lines into data
				data = file.readlines()
			if 	self.detection == 0 and self.temperate == 1:
				data[11] = '            (at-nodetected nodetected)\n'
				data[12] = '            (at-cold cold)\n'
			else:
			
				if self.detection == 1:
					data[11] = '            (at-detected detected)\n'
				else: 
					data[11] = '            (at-nodetected nodetected)\n'
				
				if self.temperate == 1:
					data[12] = '            (at-hot hot)\n'
				else: 
					data[12] = '            (at-cold cold)\n'
            				
			if self.light == 1:
				data[13] = '            (at-high high)\n'
			else: 
				data[13] = '            (at-low low)\n'
				
			if self.button == 1:
				data[14] = '            (at-press press)\n'
			else: 
				data[14] = '            (at-notpress notpress)\n'
			# now change the 2nd line, note that you have to add a newline

			# and write everything back
			with open('FF-v2.3/ProblemFinal.pddl', 'w') as file:
					file.writelines( data )

	press = 0

	p = encoder(t, m, s, press)
	p.encoder_function()

	os.chdir("/home/pi/FF-v2.3")
	os.system('./ff -o SmartCitiesFinal.pddl -f ProblemFinal.pddl > output.txt')

	os.chdir("/home/pi/python-plugwise")
	os.system('sudo python sciot_plugwise.py')
        
        if 'TURNFRONTLIGHTON' in open('../FF-v2.3/output.txt').read():
		Luminance_St = 1

	if 'TURNFRONTLIGHTOFF' in open('../FF-v2.3/output.txt').read():
                Luminance_St = 0
        try:    
        	GPIO.output(24, Luminance_St)         # set GPIO24 to 1/GPIO.HIGH/True  
        	sleep(0.5)    
            
	except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
   	 GPIO.cleanup()                 # resets all GPIO ports used by this program  

	def create_connection(db_file):
		
		try:
			conn = sqlite3.connect(db_file)
			return conn
		except Error as e:
			print(e)
	 
		return None
	 
	 
	def select_all_tasks(conn):
	 
		cur = conn.cursor()
		cur.execute("SELECT * FROM readings;")
	 
		rows = cur.fetchall()
	 
		for row in rows:
			print(row)
	 
	 
	def insert_data(conn, temperature, luminance, sensor, doorbell, datetime):
	   
		cur = conn.cursor()
		
		cur.execute("INSERT INTO readings (temperature,luminance, sensor, doorbell, datetime) values (?,?,?,?,?)", (t, m, sensor, doorbell, datetime))

		rows = cur.fetchall()
	 
		for row in rows:
			print(row)
	 
	def main():
		os.chdir("/home/pi")
		database = "sensor_rd.db"
	 
		# create a database connection
		conn = create_connection(database)
		doorbell = "0"
		
		datetime = "1201"
		sensor = "1"
		
		with conn:
			
			#print("1. Inserts sensor data")
			insert_data(conn, t, m, sensor, doorbell, datetime)
	 
			print("2. Query all tasks")
			select_all_tasks(conn)
	 
	 
	if __name__ == '__main__':
		main()
