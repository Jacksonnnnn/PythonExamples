height = raw_input("What is the height of your object in inches?  ")
weight = raw_input("What is the weight of your object in pounds?  ")

BMI = (weight / (height * weight)) * 703

print "The BMI of your object is %s." % (BMI)