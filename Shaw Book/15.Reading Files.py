from sys import argv
script, filename = argv
txt = open (filename)

print "Here's your file %r:" % filename
print txt.read()
#When the person types it again, they do not need to add double quotes.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()