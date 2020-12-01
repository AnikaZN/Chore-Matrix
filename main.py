import schedule
import time

"""
Dishes 2 days
Garbage 4 days
Sweep 5 days
Vacuum 7 days
Intense Clean 14 days
Laundry 4 days
"""

def dishes():
    print("Do the dishes today!")

def garbage():
    print("Take out the garbage today!")

def sweep():
    print("Sweep today!")

def vacuum():
    print("Vacuum today!")

def laundry():
    print("Do the laundry today")

def deep_clean():
    print("Today is a deep cleaning day!")


schedule.every(2).seconds.do(dishes)
schedule.every(4).seconds.do(garbage)
schedule.every(4).seconds.do(laundry)
schedule.every(5).seconds.do(sweep)
schedule.every(7).seconds.do(vacuum)
schedule.every(14).seconds.do(deep_clean)

while True:
    schedule.run_pending()
    time.sleep(1)
