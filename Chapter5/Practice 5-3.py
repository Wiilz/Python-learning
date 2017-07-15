print "How wide is the room?"
width = raw_input()
width = int(width) 
print "How many meters is the room?"
length = raw_input()
length = int(length)
carpetArea = 2
number = width * length / carpetArea
print "This room requires",number,"rugs"
