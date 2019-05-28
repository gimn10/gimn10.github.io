#!/Python37/python.exe
import serial
import cgi
import time

print ("STATUS: 200 OK\n")
req = cgi.FieldStorage();

ports = 54

ser = serial.Serial()
ser.port = req['p'].value
ser.baudrate = 9600
ser.timeout = 1
ser.setDTR(False)

if not ser.isOpen():
	try:
		# ser = serial.Serial(req['p'].value, 9600, timeout=1)
		ser.open()
	except: 
		print("error opening")
		exit()
else:
	print ("serial port is open")
  	
if not ser.isOpen():
	time.sleep(1.5)  # this will needed for initializing arduino
	
for port in range(ports):
	ser.write(bytes('0'+str(port)+'\n','latin'))
		
ser.write(bytes(req['c'].value+'\n','latin'))
if int(req['r'].value) == 1:
	res = '';
	while not res:
		res = ser.readline()
	print(res.decode('UTF-8'))
else:
	print ("ok")