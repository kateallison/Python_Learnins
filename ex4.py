#Defining variable names and setting out basic operations
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passengers_per_car = passengers / cars_driven

#printing statements with operators/variables in the middle of printed sentences
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Study drills
#Error was that the "carpool capacity" variable was not properly defined prior to the command.
#Here, "carpool_capacity" on line 8 was difference that "car_pool_capacity" as it
#was written in your syntax. Syntax matters, mmmmmkay?

#Study Drills
# 1. Using .0 invokes floating point numbers in all Pythons. Using 4 would have been fine
# in this case, but in other cases that might not be true.

# 2. Floating point means any number that has a value after the . Meaning, it has whole
# numbers and parts of numbers.

# 3. I'm not doing this, we all know what it means.

# 4. I know this. It's like var<-x in R

# 5. I know this. I rock underscores. I be using them all the time.

# 6. Aw, man seriously?  Ok, here, let's go.

print cars + space_in_a_car
print carpool_capacity*drivers
print float(cars_driven)/cars

#That last one messed me up because of integers. I hate those things.
#Apparently can also accomplish this my multiplying times 1.0.  Woot, knowledge!