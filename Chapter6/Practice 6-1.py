import easygui

easygui.msgbox("This program converts Fahrenheit to Celsius")
fahrenheit = float(easygui.enterbox("Type in  a temperature in Fahrenheit: "))
celsius = int ((fahrenheit - 32) * 5.0 / 9)
easygui.msgbox("This is "+ str (celsius) +" degrees Celsius")
