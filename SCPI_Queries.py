import socket
import time
import pandas as pd
import datetime as dt
#example python script for GS communication
#establishing connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(1)
s.connect(('192.168.0.149',5025))


# sending lock screen cmd (lock screen)
output = 'SYST:RWL\n'
s.send(output.encode('utf-8'))

k = 0
Voltage = []			#Create voltage empty list to append measured voltage values into it.
Current = []			# same above
Watts = []
PF = []
VA = []
times = []

def SCPI_Measurements(Voltage,Current,Watts,PF,VA,times):


	while True:

		output1 = 'MEASure:VOLTage?\n'				# Send SCPI query to measure the voltage.
		s.send(output1.encode('utf-8'))				
		msg1 = s.recv(1024)							# Set a variable to store the response in. 
		msg1 = msg1.decode('ascii')
		Voltage.append(msg1.replace('\n\x00',''))	# Remove extra information in the response (hex value, new line, etc)
		
		output2 = 'MEASure:POW?\n'					# Send SCPI query to measure power in watts.
		s.send(output2.encode('utf-8'))
		msg1 = s.recv(1024)
		msg2 = msg1.decode('ascii')
		Watts.append(msg2.replace('\n\x00',''))

		output3 = 'MEASure:PF?\n'					# Send SCPI query to measure Power factor.
		s.send(output3.encode('utf-8'))
		msg1 = s.recv(1024)
		msg2 = msg1.decode('ascii')
		PF.append(msg2.replace('\n\x00',''))
		# ti = ti + time.time()
		# times.append(ti)		
		# time.sleep(1)

		output4 = 'MEASure:POW:APP?\n'				# Send SCPI query to measure apparent power S.
		s.send(output4.encode('utf-8'))
		msg1 = s.recv(1024)
		msg2 = msg1.decode('ascii')
		VA.append(msg2.replace('\n\x00',''))

		output5 = 'MEASure:CURR?\n'					# Send SCPI query to measure current.
		s.send(output5.encode('utf-8'))
		msg1 = s.recv(1024)
		msg2 = msg1.decode('ascii')
		Current.append(msg2.replace('\n\x00',''))
		time.sleep(5)
		ti = time.time()
		ti = dt.datetime.utcfromtimestamp(ti).strftime('%Y-%m-%d %H:%M:%S')
		print(ti)
		times.append(ti)
		
		output5 = 'SYST:LOC\n'						# Unlock Gs screen
		s.send(output5.encode('utf-8'))

		# The next command is to timecode the commands sent. It's the system time (NOT GS TIME)

		#timestamp = [dt.datetime.now().replace(microsecond=0) + dt.timedelta(seconds=k+k+k+k+k) for k in range(len(times))]
		d = {'times':times,'Voltage':Voltage,'Watts':Watts,'PF':PF,'VA':VA,'Amps':Current}
		df = pd.DataFrame(d)
		df.to_csv(r'C:/Users/PowerLab_GS/Desktop/SCPI Python/SCPI_GS/Gs_Measuremetns2.csv',index = False)
		
	s.close()
SCPI_Measurements(Voltage,Current,Watts,PF,VA,times)
# print("Voltage" + SCPI_Measurements())