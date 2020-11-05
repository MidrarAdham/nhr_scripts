
import pandas as pd 
import numpy as np
'''
f = open("SCPI.text","w+")
for i in range(10):
	f.write("VOLT \n")
'''
def Frequency_text():

	f = open("MACR_SCPI.text","w+")

	col_list = [col]

	reader = pd.read_csv(file,usecols=col_list)	#Read specific column from csv file (This file should voltage profile file)

	lis = reader.values.tolist()								#Convert values to list 

	x = sum(lis,[])												#Clean data. Remove square brackets from list
	
	c = f.write("MACR:LEAR 1\n")

	c = f.write("MACR:OPER:SYNC:INST1 SYNC\n")

	c = f.write("FREQ 60\n")

	c = f.write("MACR:LEAR 0\n")

	c = f.write("MACR:RUN\n")
	
	for i in x:

		c = f.write("FREQ "+str(i)+"\n")

	print("The file is completed. Thank you")	

def Voltage_text():

	f = open("SCPI.text","w+")									#Read and write to text file

	col_list = [col]									

	reader = pd.read_csv(file,usecols=col_list)					#Read specific column from csv file (This file should voltage profile file)

	lis = reader.values.tolist()								#Convert values to list 

	x = sum(lis,[])												#Clean data. Remove square brackets from list

	for i in x:

		c = f.write("VOLT "+str(i)+"\n")

	print("The file is completed. Thank you")

def user_inputs():

	global col

	global file

	print('Choose a parameter:\n make sure to type your answser in CAPITAL LETTERS \n 1) If you wish to create frequency commands, type FREQ \n 2) If you wish to create voltage commands, type VOLT')

	x = str(input())

	para = "VOLT"

	print('Make sure the csv file in the same path as this python file')

	file = str(input('Kindly, type the name of the csv file '))

	col = str(input('Type the name of the column that the has the voltage or frequency values in '+str(file)+' file \n'))

	if not ".csv" in file:

		file+=".csv"

	if x == para:

		Voltage_text()

	else:

		Frequency_text()


user_inputs()