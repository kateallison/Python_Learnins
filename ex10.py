#Escape double quotes. I was literally just wondering how you would do this.
#Maybe I'm a mind reader. Or a book reader. Or just a Python predictor :)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Output
#	I'm tabbed in.
#I'm split
#on a line.
#I'm \ a \ cat.

#I'll do a list:
#	* Cat food
#	* Fishies
#	* Catnip
#	* Grass

#Note to self: print and review resource on escape sequences.

#Fun code

#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" %i,
#[Commented out for exercises below]
		
#Output
#IT SPINS, EHRMEGERD.

#Study drills
#1. Ok, flash cards. I think not that. But I'll make a list and study it.
#2. Use ''' instead (below). It looks the same. Great. 
#but """ allows escape sequences. ''' does not

#tabby_cat = "\tI'm tabbed in."
#persian_cat = "I'm split\non a line."
#backslash_cat = "I'm \\ a \\ cat."

#fat_cat = '''
#I'll do a list:
#\t* Cat food
#\t* Fishies
#\t* Catnip\n\t* Grass
#'''

#print tabby_cat
#print persian_cat
#print backslash_cat
#print fat_cat

#3. 
