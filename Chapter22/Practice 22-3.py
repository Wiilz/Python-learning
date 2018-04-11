import pickle

name = raw_input("What's your name:")
age = raw_input("What's your age?")
color = raw_input("What's your favorite color?")
food = raw_input("What's your favorite food?")

inf_list = []
inf_list.append(name)
inf_list.append(age)
inf_list.append(color)
inf_list.append(food)

my_inf = open("information.pkl",'w')
pickle.dump(inf_list,my_inf)
my_inf.close()
