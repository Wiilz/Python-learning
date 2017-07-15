import easygui

name = easygui.enterbox ("What's your name?")
street = easygui.enterbox ("Which street do you live in?")
city = easygui.enterbox ("Which city do you come from?")
postcode = easygui.enterbox ("What's your postcode?")

easygui.msgbox( "Here is your dress:\n "+ name +"\n"+ street + "\n"+ city + "\n"+ postcode + "\n")
