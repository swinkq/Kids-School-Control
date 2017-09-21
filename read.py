import MFRC522
import signal
import os
import time

continue_reading = True
MIFAREReader = MFRC522.MFRC522()

cardA = [224,96,42,137,35]
cardB = [176,203,130,124,133]
cardC = [20,38,121,207,132]

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)

while continue_reading:
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  if status == MIFAREReader.MI_OK:
    print "Card detected"
  (status,backData) = MIFAREReader.MFRC522_Anticoll()
  if status == MIFAREReader.MI_OK:
    print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
    if  backData == cardA:
      print "Vasea Pupkin"
      os.system("python /home/pi/SPI-Py/MFRC522-python/greenled.py 2>/dev/null")
      date_string = time.strftime("%Y-%m-%d-%H:%M:%S")
      os.system("./sending.sh 069062726 'Vasea at school-'" + date_string)



    elif backData == cardB:
      print "Vlad Lazari"
      os.system("sshpass -p a ssh root@10.14.0.60 fbi -T 1 -d /dev/fb1 -noverbose /home/pi/Documents/pic/vl.jpg")
      os.system("sshpass -p a ssh root@10.14.0.60 /home/pi/Documents/open.sh 2>/dev/null")
 #     os.system("sshpass -p a ssh root@10.14.0.60 sleep 2")
      os.system("sshpass -p a ssh root@10.14.0.60 killall fbi")
    elif backData == cardC:
      print "is Card C"
    else:
      print "wrong Card"
      os.system("python /home/pi/SPI-Py/MFRC522-python/redled.py 2>/dev/null")
