import time
#from time import gmtime
a = time.strftime('%H:%M:%S')
b= int(time.strftime ('%H'))
print(a)
if(b>=12 and b<4):
        print("sleeping time ")
if(b>4 and b<6):
        print("study time")
if(b>6 and b<9):
        print("breakfast, exercise 💪 time")
if(b>9 and b<14):
        print("library time")
if(b>14 and b<20):
        print("class time")
if(b>20 and b<00):
        print(" rest time and dinner time")
