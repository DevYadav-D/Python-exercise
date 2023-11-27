import re
def add_time(startingTime, addTime, *arg):
    startingTime = re.split(r'[:\s]',startingTime)
    addTime = re.split(r'[:\s]', addTime)
    if "PM" in startingTime:
        hours = 12
    else:
        hours = 0
    minutes = int(startingTime[1])+int(addTime[1])
    hours = hours + minutes//60
    minutes = minutes%60
    hours = hours + int(startingTime[0])+int(addTime[0])
    if ((hours//12)%2 == 0):
        timeformat = "AM"
    else:
        timeformat = "PM"
    days = hours//24
    hours = hours%12
    if days<2:
        output = str(hours)+":"+str(minutes)+" "+timeformat
    else:
        output = str(hours)+":"+str(minutes)+" "+ timeformat+" ("+str(days)+" days later)"
    print(output)
            
    return 1

add_time("3:00 PM", "03:10")
# Returns: 6:10 PM