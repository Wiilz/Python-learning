import easygui

password = easygui.enterbox("Please your password:")
if password == 'hello':
    easygui.msgbox("You are in!")
    tank = float(raw_input("Size of tank:"))
    full = float(raw_input("percent full:"))
    far = float(raw_input("km per liter:"))
    canGo = (tank-5) * (full/100) * far
    print "You can go another",canGo,"km."
    if canGo >= 200:
        print "The next gas station is 200 km away,You can wait for the next station."
    else:
        print "The next gas station is 200 km away,Get gas now!"
else:
    easygui.msgbox("wrong password!")
