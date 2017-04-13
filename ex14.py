#ex14.py = Prompting and Passing
#https://learnpythonthehardway.org/book/ex14.html

#from sys import argv

#script, user_name = argv
#prompt = '>'

#print "Hi %s, I'm the %s script." % (user_name, script)
#print "I'd like to ask you a few questions."
#print "Do you like me %s?" % user_name
#likes = raw_input(prompt)

#print "Where do you live %s?" % user_name
#lives = raw_input(prompt)

#print "What kind of computer do you have?"
#computer = raw_input (prompt)

#print """
#Alright, so you said %r about liking me.
#You live in %r. Not sure where that is.
#And you have a %r computer. Nice.
#""" % (likes, lives, computer)

#HQSML-150831:Desktop kallis201$ python ex14.py Kate
#Hi Kate, I'm the ex14.py script.
#I'd like to ask you a few questions.
#Do you like me Kate?
#>Yes
#Where do you live Kate?
#>Philadelphia
#What kind of computer do you have?
#>Mac

#Alright, so you said 'Yes' about liking me.
#You live in 'Philadelphia'. Not sure where that is.
#And you have a 'Mac' computer. Nice.

#Zork! Adventure! I remember this.

#Try it out

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s awesome-o 5000 question asker." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you have any coffee %s?" % user_name
coffee = raw_input(prompt)

print "Are you wearing pants at work today, %s?" % user_name
pants = raw_input(prompt)

print "How many dragons do you have?"
dragons = raw_input (prompt)

print "Can I play with your pet dragons?"
play = raw_input (prompt)

print """
Alright, so you said %r about having coffee. I have no coffee. You should bring me some.
You said %r about pants wearing. Interesting.
And you have %r dragons. Nice.  You said %r about playing with them. Rude. 
You should have said 'Hell, yes'.
""" % (coffee, pants, dragons, play)






