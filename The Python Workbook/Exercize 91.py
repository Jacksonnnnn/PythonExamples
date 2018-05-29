def precedence(s):
	if s == "+" or s == "-":
		print "1"
		return
	if s == "*" or s == "/":
		print "2"
		return
	if s == "^":
		print "3"
		return
	else:
		print "-1"
		return
		
def main():
	s = raw_input("Enter an operation...  ")
	precedence(s)
main()