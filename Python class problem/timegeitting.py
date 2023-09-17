import time
ab = time.strftime('%H:%M:%S')
a = int(time.strftime('%H'))
print(ab)
if(a>=4 and a<6):
   print("AM,Early Morning")
if(a>=6 and a<12):
   print("AM,Good morning")
if(a>=12 and a<14):
   print("PM,Good Afternoon")
if(a>=14 and a<19):
   print("Good Evening")
if(a>=19 and a<=23):
   print("PM,Good Night")
if(a>=00 and a<=3):
   print("AM,Midnight")