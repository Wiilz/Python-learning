my_file = open('notes.txt','r')
first_line = my_file.readline()
second_line = my_file.readline()
print "first line = ", first_line
print "second line = ", second_line
my_file.close()
