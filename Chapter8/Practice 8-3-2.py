i = int(raw_input("Which multiplication table would you like?"))
j = int(raw_input("How high do you want to go?"))
print "Here's your table:"
k = 1
while k <= j:
    print i,"*",k,"=",i*k
    k = k+1
