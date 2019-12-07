import datetime
import sys
import notify2 
import time
import playsound

hour = sys.argv[1]
min_n = sys.argv[2]
message =  sys.argv[3]
def notifier(hour_n,min_n,message):
	notify2.init("Reminder")
	n = notify2.Notification(None,icon = "")
	from playsound import playsound
	n.set_urgency(notify2.URGENCY_NORMAL)
	n.update("Reminder",message)
	n.show()
	playsound('bell.mp3')
	exit(0)
while (int(datetime.datetime.now().strftime('%H'))<=int(hour) and int(datetime.datetime.now().strftime('%M'))<=int(min_n)):
	#print ("*")
	time.sleep(1)
	if (int(datetime.datetime.now().strftime('%H'))==int(hour) and int(datetime.datetime.now().strftime('%M'))==int(min_n)):
		notifier(hour,min_n,message)