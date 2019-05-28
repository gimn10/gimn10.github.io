#!/Python37/python.exe
import serial
import cgi
import time

print ("STATUS: 200 OK\n")
req = cgi.FieldStorage();

ports = 54
startval = 17

ser = serial.Serial()
ser.port = req['p'].value
ser.baudrate = 115200
ser.timeout = 1
ser.setDTR(False)

if not ser.isOpen():
	try:
		# ser = serial.Serial(req['p'].value, 9600, timeout=2)
		ser.open()
	except: 
		print("error opening")
		exit()
else:
	print ("serial port is open")
  	
if not ser.isOpen():
	time.sleep(1.5)  # this will needed for initializing arduino        

if req['c'].value == '00':
        for port in range(startval, ports):
                ser.write(bytes('1'+str(port)+'\n','latin'))                
                time.sleep(0.05)
                ser.write(bytes('0'+str(port)+'\n','latin'))
        for por in range(startval, ports):
                ser.write(bytes('1'+str(por)+'\n','latin'))
        time.sleep(0.6)

        for po in range(startval, ports):
                ser.write(bytes('0'+str(po)+'\n','latin'))
                
ser.write(bytes(req['c'].value+'\n','latin'))
if int(req['r'].value) == 1:
	res = '';
	while not res:
		res = ser.readline()
	print(res.decode('UTF-8'))
else:
	print ("ok")
