#The following lines print text within quotes. %s is a replacement string.
#Line 5 (*10) will print 10 periods in a line following the other two prints.
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "." * 10 #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#pay attention to commas, yo
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

#you get this (output):
#Mary had a little lamb.
#Its fleece was white as snow.
#..........
#Cheese Burger

#without the comma, you get this (output):
#Mary had a little lamb.
#Its fleece was white as snow.
#..........
#Cheese
#Burger

#clearly commas make it where the text continues on the same line. Woot!

#Questions
#1. Comments. Check.
#2. I did this. It was useful. I can't spell.
#3. I wrote down my mistake. It was from typing too fast. Also, cool nerd notebook.
#4. I think that's a fair request. Fewer mistakes = winning!
#5. I totally know they make mistakes. I am married to a code mistake maker :)

#Also, it flags unmatched parentheses (like this ")) when it finds one. Yay!