#Strings and Text.  WAHOOOOOO!
#Defining variable names and setting out basic operations

#defining x with a replacement digit inside
x = "There are %d types of people." % 10

#defining strings
binary = "binary"
do_not = "don't"

#defining a string with a replacement string inside and telling it what to do. Woot.
y = "Those who know %s and those who %s." % (binary, do_not)

#print that ish
print x
print y

#print that ish, replace the %r with the value of x
print "I said: %r." % x
print "I also said: '%s'." % y

#Define variable "hilarious" with the string "False"

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e

#FIRST TRY, BITCHES!
#Strings were put inside of strings on lines 19, 20 25, 27
#Because adding two things together makes the sum of those things happen. 
#Here, those things are both semi-long, so now they're super-long.

