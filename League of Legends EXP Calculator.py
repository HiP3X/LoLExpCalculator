#implementing a better round function
def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
      a = num[:-2-(not dec)]       # integer part
      b = int(num[-2-(not dec)])+1 # decimal part
      return float(a)+b**(-dec+1) if a and b == 10 else float(a+str(b))
    return float(num[:-1])
#here we define start
def start():
    print()
    #summoner lvl selection
    print("Select Summoner lvl:")
    print("1)1-9")
    print("2)10-19")
    print("3)20-29")
    print("4)30+")
    pick = input()
    print("Enter game length(eg;13:45)")
    time = input()
    #converting time from mm:ss to only seconds
    timeInMin = time[:+2]
    timeInSec = time[3:]
    totalTime = ((int(timeInMin)*60) + int(timeInSec))
    if(pick == '1'):
       #calculating exp gained baseod on the official riot formula
       time1 = (float(totalTime)*0.11)+6.6
       print("xp gained:")
       time1 = int(proper_round(time1))
       print(time1)
       start()
    if(pick == '2'):
      #calculating exp gained baseod on the official riot formula
      time2 = (float(totalTime)*0.11)+6.6
      print("XP gained:")
      #reducing exp by 10%
      time2 = float(time2)*0.9
      time2 = int(proper_round(time2))
      print(time2)
      start()
    if(pick == '3'):
        #calculating exp gained baseod on the official riot formula
        time3 = (float(totalTime)*0.11)+6.6
        print("XP gained:")
        #reducing exp by 20%
        time3 = float(time3)*0.8
        time3 = int(proper_round(time3))
        print(time3)
        start()
    if(pick == '4'):
        #calculating exp gained baseod on the official riot formula
        time4 = (float(totalTime)*0.11)+6.6
        print("XP gained:")
        #redusing exp bu 35%
        time4 = float(time4)*0.75
        time4 = int(proper_round(time4))
        print(time4)
        start()
start()
