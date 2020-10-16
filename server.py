import csv
import socket					#Import libraries
import time
'''
import SCPI_functions as scpi
s = scpi.conn()
scpi.conn()

'''

def conn(): 		#This function establishes connection and lock the touch panel screen.
	global s		#Assigning variable as global, means it can be used out of this function.
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(1000)
	s.connect(('192.168.0.149',5025)) # NHR 9410 IP address
	output = 'SYST:RWL\n'			  # Lock the touch panel screen (Safety purpose)
	s.send(output.encode('utf-8'))	  # For each SCPI command, it MUST encoded into utf-8.
	return s
def clos(s):							  # This function is meant to close the connection
	output5 = 'SYST:LOC\n'			  # Unlock the touch panel screen
	s.send(output5.encode('utf-8'))
	s.close()						  # Close the connection