import random
import math
def weekly_scheduler():

 sched = input("Weekly Scheduler, press enter...")
 taskers = ["1st tasker","2nd tasker","3rd","4th","5th","6th","7th"]; 
 random.shuffle(taskers)
 tasks =[None]*len(taskers); 
 for i in range(0, len(taskers)):
     tasks[i] = taskers[i]; 
 bottom_floor = tasks[1]
 stairs_toilet_bottom_floor = tasks[2]
 floor_1_toilet = tasks[3]
 garbadge_street = tasks[4]
 print("Bottom Floor:" + bottom_floor)
 print("Stairs and Toilet:" + stairs_toilet_bottom_floor)
 print("1st Floor Toilet:" + floor_1_toilet)
 print("Garbadge on Thursdays:" + garbadge_street)
 weekly_scheduler()
weekly_scheduler()
