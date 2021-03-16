import random
import math
def weekly_scheduler():

 Weekly_scheduler = input("Weekly Scheduler, press enter...")
 Taskers = ["Rogerio","Marilia","Moncarcha","Lopes","Gui","Valter","Kika"]; 
 random.shuffle(Taskers)
 Functions =[None]*len(Taskers); 
 for i in range(0, len(Taskers)):
     Functions[i] = Taskers[i]; 
 bottom_floor = Functions[1]
 stairs_toilet_bottom_floor = Functions[2]
 floor_1_toilet = Functions[3]
 garbadge_street = Functions[4]
 print("Bottom Floor:" + bottom_floor)
 print("Stairs and Toilet:" + stairs_toilet_bottom_floor)
 print("1st Floor Toilet:" + floor_1_toilet)
 print("Garbadge on Thursdays:" + garbadge_street)
 weekly_scheduler()
weekly_scheduler()
