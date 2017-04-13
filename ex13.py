#ex13.py = Parameters, Unpacking, Variables
#https://learnpythonthehardway.org/book/ex13.html

#"python ex13.py" is an argument. Check.

from sys import argv

script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

#HQSML-150831:Desktop kallis201$ python ex13.py first 2nd 3rd
#The script is called: ex13.py
#Your first variable is: first
#Your second variable is: 2nd
#Your third variable is: 3rd

#HQSML-150831:Desktop kallis201$ python ex13.py stuff things that
#The script is called: ex13.py
#Your first variable is: stuff
#Your second variable is: things
#Your third variable is: that

#HQSML-150831:Desktop kallis201$ python ex13.py kiwi banana peach
#The script is called: ex13.py
#Your first variable is: kiwi
#Your second variable is: banana
#Your third variable is: peach

#I already made the cautionary error because reasons.
#Modules. Check.

#My own try.

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first spirit animal is:", first
#print "Your second spirit animal is:", second
#print "Your third spirit animal is:", third

#cat = raw_input ("How many cats do you have? ")
#dog = raw_input ("How many dogs do you have? ")
#monkey = raw_input("How many monkeys do you have? ")

#print "So, you have %r cats, %r dogs, and %r monkeys.  Little light on the monkeys there, dude." % (
#	cat, dog, monkey)
	
#	script, first, second, third = argv

print "The script is called:", script
print "Your first spirit animal is:", first
print "Your second spirit animal is:", second
print "Your third spirit animal is:", third

cat = raw_input ("How many cats do you have? ")
dog = raw_input ("How many dogs do you have? ")
monkey = raw_input("How many monkeys do you have? ")

print "So, you have %s cats, %s dogs, and %s monkeys.  Little light on the monkeys there, dude." % (
	cat, dog, monkey)