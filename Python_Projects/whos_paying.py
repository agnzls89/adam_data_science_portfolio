#Banker roulette
#Program to randomly choose the person that is paying the bill
#input a list of names
#split the names by delimiter ","
#use random.choice() to select the person at random that will pay the bill

import random
names = input("Give me the list of persons at the table (separated by commas): ")

list_names = names.split(',')

choice = random.choice(list_names)
print("{}, you are paying the bill.".format(choice))