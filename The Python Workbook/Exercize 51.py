#Asking the grade of the user.
lgrade = raw_input("What is your letter grade?  ")

#Using the letter grade to get the Grade Point for the class.
if lgrade == "A+":
	print "Congratulations! Your grade points are at a 4.0."
elif lgrade == "A":
	print "Congratulations! Your grade points are at a 4.0."
elif lgrade == "A-":
	print "Good work, but your grade points are only 0.3 points away from a 4.0 (You have a 3.7). You can do it!"
elif lgrade == "B+":
	print "You're doing good work, but we want to see that A+! You have a 3.3."
elif lgrade == "B":
	print "You're doing good work, but we want to see that A+! You have a 3.0."
elif lgrade == "B-":
	print "You have a 2.7. We need to improve that grade more, but you're still doing an amazing job. Keep up the good work!"
elif lgrade == "C+":
	print "You're falling under the curve. At least shoot for a B-. You have a 2.3."
elif lgrade == "C":
	print "Start studying, because you're going to need it... Don't fall under a C or things will get bad in the future. You have a 2.0"
elif lgrade == "C-":
	print "A 1.7 will not get you any scholarship money for collage and isn't the best grade to have when applying for jobs."
elif lgrade == "D+":
	print "This 1.3 is unacceptable. You need to hit the books. If you play sports, you're about to get kicked off the team."
elif lgrade == "D":
	print "One letter grade from a F which is failing. In some schools and districts, a D is failing. This is a 1."
elif lgrade == "F":
	print "Get your act together man. School greatly impacts the future. You want to make bank, be in the NFL, NBA, you've gotta get good grades. This counts as a 0."