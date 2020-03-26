import time
import datetime
import webbrowser
d=datetime.datetime.today()
g=d.isoweekday()
#Scheduled item pages links
a='https://aa.com' 
b='https://bb.com'
c='https://cc.com'
def ggd(a, b, c):
	print("gg")
	time.sleep(1)
#login page
	webbrowser.open_new_tab('https://auto.com') 
	time.sleep(7)
	webbrowser.open_new_tab(a)
	time.sleep(1)
#checking the day of the week (if there is no subject in the schedule, then there will be no link)
	if g==1 or g==3 or g==4 or g==6:
		webbrowser.open_new_tab(b)
		time.sleep(1)
		if g==1:
			webbrowser.open_new_tab(c)
			time.sleep(1)
	while True:
		tm=int(time.mktime(datetime.datetime.now().timetuple()))
		print("gg "+str(tm))
#how often to visit a site in seconds
		while int(time.mktime(datetime.datetime.now().timetuple()))<tm+3600:
			time.sleep(3)
#current time in seconds
			print(int(time.mktime(datetime.datetime.now().timetuple())))
		if int(time.mktime(datetime.datetime.now().timetuple()))>tm+3601 and int(time.mktime(datetime.datetime.now().timetuple()))<tm+3614:
			print("gg")
			webbrowser.open_new_tab(a)
			time.sleep(1)
#checking the day of the week (if there is no subject in the schedule, then there will be no link)
			if g==1 or g==3 or g==4 or g==6:
				webbrowser.open_new_tab(b)
				time.sleep(1)
				if g==1:
					webbrowser.open_new_tab(c)
					time.sleep(1)

#you can add a larger number of links depending on the total number of subjects and pass them as arguments to the function
if g==1:
	ggd(a, b, 0)
elif g==2:
	ggd(a, 0, 0)
elif g==3:
	ggd(a, b, 0)
elif g==4:
	ggd(a, b, 0)
elif g==5:
	ggd(a, 0, 0)
elif g==6:
	ggd(a, b, 0)
else:
	print("ggssg")
