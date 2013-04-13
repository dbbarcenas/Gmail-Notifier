import serial, sys, feedparser
#Settings - Change these to match your account details
USERNAME="XXXXXXX@gmail.com"
PASSWORD="PASSWORDXXWD"
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"
SERIALPORT = "/dev/tty.usbserial-FTE3RS4J" # Change this to your serial port!
# Set up serial port
try:
	ser = serial.Serial(SERIALPORT, 9600)
except serial.SerialException:
	print "no device connected - exiting"
	sys.exit()

newmails = int(feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)["feed"]["fullcount"])
   
# Output data to serial port
if newmails > 0: 
	ser.write("m")
	print "some mail"
else: 
	ser.write("n")
	print "no mail" 
#print data to terminal


# Close serial port
ser.close()
 