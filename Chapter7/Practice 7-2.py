gender = raw_input("Please enter gender:")
if gender == 'f' :
    age = int(raw_input("Please enter age:"))
    if 10<=age<=12:
        print ("You can enter the team")
    else:
        print("Sorry,you can't enter the team.")
else:
    print ("Sorry,you can't enter the team.")
