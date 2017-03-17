#Defining variable names and setting out basic operations
my_name = 'Kate Allison'
my_age = 35
my_height = 70 #inches
my_weight = 180 #lbs. haha. fuck you.
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Streaky'

print "Let's talk about %s." %my_name
print "She's %d inches tall." %my_height
print "She's %d pounds light." %my_weight
print "Actually that's not too heavy" #yeah, right.
print "She's got %s eyes and %s hair" % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the amount of coffee." % my_teeth

#tricksy line
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
	
#First try!

# 1. I get why, my find and replace fixes this.
# 2. %r is print no matter what, %f is for floating point numbers
#	%e engineering notation (ew), plus other scary things.
#	if you say %02d, it will ensure everything has at least 2 digits, potentially adding 0s

#Testing
#Testing!
#tricksy line
print "If I add %02d, %03d, and %04d I get %05d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
#Note to self: THIS SHIT IS SUPER FUCKING USEFUL FOR DATA STUFF.
#3. Google. Check.

