#############
# Variables #
#############
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

####################
# Print Statements #
####################
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#If you look at the print statments, you'll see that every variable that needs to be printed is seperated by ", (VARIABLE),".

########################
#Calculator Study Drill#
#    With Variables    #
########################
b = 4*19
i = 3+4
print "What is 3j+4j? ", i, "j."
print "Okay, what about 4b*19b? ", b, "b."