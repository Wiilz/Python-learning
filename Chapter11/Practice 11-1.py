import time

num = int(raw_input("How many seconds ?"))
for i in range(num, 0 ,-1):
    print i
    time.sleep(1)
print "BLAST OFF!"
