print "How wide is the room?"
width = raw_input()
width = int(width)

print "How many meters is the room?"
length = raw_input()
length = int(length)

carpetArea = 2
print "What is the price of each carpet?"
carpetPrice = raw_input()
carpetPrice = int(carpetPrice)

number = width * length / carpetArea
print "This room requires",number,"rugs"

price = number * carpetPrice

print "These carpets cost",price,"yuan"
