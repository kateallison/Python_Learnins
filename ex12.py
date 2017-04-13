#ex12.py = Prompting People
#https://learnpythonthehardway.org/book/ex12.html

#example: y = raw_input ("Name? ")

age = raw_input ("How old are you? ")
height = raw_input ("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall, and %r heavy." % (
	age, height, weight)
	
#pydoc 
#Help on built-in function raw_input in module __builtin__:

#raw_input(...)
    #raw_input([prompt]) -> string
    
    #Read a string from standard input.  The trailing newline is stripped.
    #If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    #On Unix, GNU readline is used if enabled.  The prompt string, if given,
    #is printed without a trailing newline before reading.
#(END)

#Typing Q for quit!

#Online search of Pydoc
#It's like "help" in R.

#I have read things about "file, open, os, and sys".  I believe I understand them,
#But I can ask for help too :)

#Reminder
# %r is for debugging and %s is for display.

