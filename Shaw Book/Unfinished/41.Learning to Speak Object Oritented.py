import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function names *** that takesself and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

#Do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

#Load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())
	
def convert(snippit, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippit.count("%%%"))]
	
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	for sentence in snippet, phrase:
		result = sentence[:]
	
		#fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
		
		#fake other names
		for word in other_names:
			result = reult.replace("***", word, 1)
	
		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
		
		results.append(result)
	
	return results

	#keep it going until they hit CTRL-D
	try:
		while True:
			snippets = PHRASES.keys()
			random.shuffle(snippets)
			
			for snippet in snippets:
				phrase = PHRASES[snipet]
				question, answer = convert(snippet, phrase)
				if PHRASE_FIRST:
					question, answer = answer, question
				
				print question
				raw_input("> ")
				print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"