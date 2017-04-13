#ex11.py = Asking Questions
#https://learnpythonthehardway.org/book/ex11.html

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#[Take note of the commas at the end of the line]
#Mistake I made: % instead of %r is the wrong type of argument and this errors out.

#Defining "raw_input"
#Note: in Python 3, it's just "input". Apparently there are security issues?

#Other uses might be surveys where you want people to check their answers (assuming you 
#can store the data somehow?

#On my own.
print "How many cats do you own?",
cat = raw_input()
print "How many dogs do you own?",
dog = raw_input()
print "Day drinking: a great idea, or the greatest idea?",
booze = raw_input()

print "So, you have %r cats, %r dogs and think day drinking is %r. Let's be friends" % (
	cat, dog, booze)

