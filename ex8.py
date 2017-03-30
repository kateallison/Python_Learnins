#Whoa. Format.

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

#Note, I left off a comma and the whole thing wouldn't run because there 
#weren't enough arguments.  Interesting note.

#Output
#1 2 3 4
#'one' 'two' 'three' 'four'
#True False False True
#'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
#'I had this thing.' 'That you could type up right.' "But it didn't sing." 
#'So I said goodnight.'

#Note to self that %r = raw programmers version of the variable.
#Also, Boolean is back! And I got it right this time :)

#Study drills question #2 was confusing to me. Let's chat about that please.

