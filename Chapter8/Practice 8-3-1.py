i = int(raw_input("Which multiplication table would you like?"))
j = int(raw_input("How high do you want to go?"))
print "Here's your table:"

for j in range(1,j+1):
    print i,"*",j,"=",i*j
