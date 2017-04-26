#Ch. 15: Reading Files

# $python ex15.py ex15_sample.txt

from sys import argv

script, filename = argv

txt = open(filename)

print "Type your file %r:" %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input ("> ")

txt_again = open(file_again)

print txt_again.read()

#run pydoc open to get information about open
#opens any kind of file, but does not handle how to process the data of a file.
#won't display, creates file descriptor, where you can access the contents.

