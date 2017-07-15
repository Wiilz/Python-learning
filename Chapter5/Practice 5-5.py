print "How many cents do you have?"
fiveCents = raw_input()
fiveCents = int (fiveCents)
print "How many two cents do you have?"
twoCents = raw_input()
twoCents = int (twoCents)
print "How many five cents do you have?"
cents = raw_input()
cents = int (cents)

money = 5 * fiveCents + 2 * twoCents + cents
print "You have",money,"cents"


#参考答案
quarters = int(raw_input("How many quarters? "))
dimes = int(raw_input("How many dimes? "))
nickels = int(raw_input("How many nickels? "))
pennies = int(raw_input("How many pennies? "))
total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01* pennies
print "You have a total of: ",total
