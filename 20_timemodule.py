import time

timeatstartofcode=time.time()
print(timeatstartofcode)
i=0
while(i<5):
    print("Priyanshu")
    time.sleep(1)                #program sleeps for 3 secs.
    i=i+1
timeatendofcode=time.time()-timeatstartofcode
print(timeatendofcode)

instatneousorlocaltime=time.asctime(time.localtime(time.time()))
print(instatneousorlocaltime)


instatneousorlocaltime1=time.localtime(time.time())
print(instatneousorlocaltime1)
