nameList = []
print "Enter 5 names:"
for i in range(5):
    name = raw_input()
    nameList.append(name)
print "The names are",nameList

num = int(raw_input("Replace one name.Which one?(1-5):"))
nameList[num-1] = raw_input("New name:")
print "The names are",nameList
