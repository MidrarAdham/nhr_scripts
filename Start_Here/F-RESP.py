

import socket					#Import libraries
import time

#establishing connection to NHR 9410

def conn(): 		#This function establishes connection and lock the touch panel screen.
	global s		#Assigning variable as global, means it can be used out of this function.
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(1)
	s.connect(('192.168.0.149',5025)) # NHR 9410 IP address
	output = 'SYST:RWL\n'			  # Lock the touch panel screen (Safety purpose)
	s.send(output.encode('utf-8'))	  # For each SCPI command, it MUST encoded into utf-8.
	#return s
def clos():							  # This function is meant to close the connection
	output5 = 'SYST:LOC\n'			  # Unlock the touch panel screen
	s.send(output5.encode('utf-8'))
	s.close()						  # Close the connection

#def loop():

vals = [40, 500, 55, 60, 70]		   # Aribtrary frequency values.
output2 = 'FREQ '					   # SCPI command to set the frequency. (Pay attention to the space after the word "FREQ")
for i in vals:						   # For loop to iterate through each value in ' vals' array
	time.sleep(5)
	x = 0							   # Set a flag. If x is 0, turn on the device.
	if x == 0:
		conn()						   # Call the function that establishes the connection to the equipment
		#s.send('*WAI \n'.encode('utf-8'))
		s.send('OUTPUT ON \n'.encode('utf-8'))		# SCPI command to turn the equipment ON
		clos()										# Close the connection to execute the above command
	conn()
	time.sleep(5)
	var = output2 + str(i)+'\n'						# var is the variable used to set the frequency values
	print(var)										# Printing out the freq values just to make sure the for loop is working as expected.
	x = 1											# Set a flag. If x is 1, turn OFF the equipemnt
	s.send(var.encode('utf-8'))
	s.send('FREQ?\n'.encode('utf-8'))				# SCPI command the ask the equipment about the frequency value to make sure the values in the array are executed and inserted into the equipment.
	msg = s.recv(1024).decode()
	print('response: ',msg)							# Print the response from the equipemnt
	#clos()
	if x == 1:
		conn()
		#s.send('OUTPUT OFF \n'.encode('utf-8'))
		clos()
