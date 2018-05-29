#
# Game Map
#
#Home
#School
#Alien Ship
#Bosses Room
#Home
class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
class Death(Scene):
	quips = [
		"You died.  You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
class Home(Scene):
	def enter(self):
		print "\"Good Morning Sunshine! It's time to get up for school. You can't be late for"
		print "your big presentation in first period... you worked so hard on it! Let's go"
		print "downstairs for breakfast and we'll discuss it and go all over your points and"
		print "do everything you need to do.\" - Mom"
		print "You walk downstairs and go to the kitchen to eat. You see that your mom made"
		print "Eggs, Bacon, Tosat, Waffles, and Cereal... which do you want to eat this morning?"
		
		action = raw_input("> ")
		
		if action == "eggs":
			print "Your mom gives you eggs fresh out of the skillet, adds salt and pepper, and"
			print "gives you a fork to eat it with."
			print "\"So what do you need to do to go over your presentation?\""
			
			actiontwo = raw_input("> ")
			
			if actiontwo == "go over presentation":
				print "You spend 20 minutes going over your presentation and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
			elif actiontwo == "I think I'm okay" or "I'm okay":
				print "You spend 20 minutes watching your favorite youtuber and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
		elif action == "bacon":
			print "Your mom gives you some nice sizzling bacon, right out the pan the way you"
			print "love it. You tell her thank you can you start eating with her."
			print "\"So what do you need to do to go over your presentation?\""
			
			actiontwo = raw_input("> ")
			
			if actiontwo == "go over presentation":
				print "You spend 20 minutes going over your presentation and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
			elif actiontwo == "I think I'm okay" or "I'm okay":
				print "You spend 20 minutes watching your favorite youtuber and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
		elif action == "toast":
			print "Your mom waits two minutes for toast to be done and golden for you. \"Butter"
			print "or Creme?\" She asks. You say no and wait for it to be done."
			print "\"So what do you need to do to go over your presentation?\""
			
			actiontwo = raw_input("> ")
			
			if actiontwo == "go over presentation":
				print "You spend 20 minutes going over your presentation and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
			elif actiontwo == "I think I'm okay" or "I'm okay":
				print "You spend 20 minutes watching your favorite youtuber and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
		elif action == "waffles":
			print "Your mom puts some waffles in the toaster and heats them up for you. \"Do you"
			print "want butter?\" You decline and wait for her to give you your waffles."
			print "\"So what do you need to do to go over your presentation?\""

			actiontwo = raw_input("> ")
			
			if actiontwo == "go over presentation":
				print "You spend 20 minutes going over your presentation and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
			elif actiontwo == "I think I'm okay" or "I'm okay":
				print "You spend 20 minutes watching your favorite youtuber and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
		elif action == "cereal":
			print "You decide to make it yourself. You go to the pantry and grab the box of Fruity"
			print "Pebbles, poor them into the bowl, pour milk into the bowl, grab a spoon, and"
			print "start eating."
			print "\"So what do you need to do to go over your presentation?\""
			
			actiontwo = raw_input("> ")
			
			if actiontwo == "go over presentation":
				print "You spend 20 minutes going over your presentation and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
			elif actiontwo == "I think I'm okay" or "I'm okay":
				print "You spend 20 minutes watching your favorite youtuber and realize you're"
				print "late! You forgot what time it was and forgot that your presentation is"
				print "in first period. You run out the door, start your car, and rush to school."
				return 'School'
class School(Scene):
	def enter(self):
		print "Rushing into the door and to your classroom on the opposite side of the school, you're"
		print "trying your best to make sure that you'll make it. You feel in your pockets as you run"
		print "to class to make sure you have the USB drive, the paper, and your phone. That's all you needed."
		print "Ding... ding... ding... You made it to class, just in time."
		print "\n \"Alright guys, we're going to start with our presentations. We'll go in Alphabetical Order..."
		print "so that means, Jenny Addison, you'll be going first. Please take 2-3 minutes to set up and prepare.\""
		print "You say okay and your presentation goes smoothly. You give facts about the anatomy of a human body,"
		print "explain your thoughts completely, and give out treats to the class as examples. \"A+, next\""
		print "\nOn your way to second period, you hear a thunder in the hall way and ignore it. Once you get to"
		print "your class, you feel the earth shaking benethe your feet. Everyone else felt it too... what's going on?"
		print "Out of no where, an alien space ship appears and you back up along with everyone else to their classrooms"
		print "The alien comes in and says \"Jenny Addison... I need you to come with me pronto.\""
		
		action = raw_input("Do you want to go with the alien to his ship?> ")
		
		if action == "no":
			print "He decides to shoot your classroom claiming that you're not there and you die in the process."
			return 'death'
		if action == "yes" or "sure":
			print "Okay, you go with him to his spaceship."
			return 'spaceship'
class SpaceShip(Scene):
	def enter(self):
		print "Suddenly, you appear in their spaceship. It's green, and smells discusting. You look around to see"
		print "what they're going to do to you. You see a table with hand/foot cuffs on it. Your eyes widen."
		print "The man who is holding you says:"
		print "Idjn adjkn abhfb afie hdja jhdn iwhdn kemsif"
		print "Which the translator says \"He says he that you will be chopped up and your brain will be studied.\""
		print "You start to wiggle around, trying to get out of his grip. A little more... and you're out of his hands."
		print "You assume your fighting position. When the alien runs at you with his gun, you do a kick + punch combo."
		print "You hit the alien straight in the chest and upper theigh. Now you have to fight the translator who is"
		print "much bigger than the first guy. What will you do?"
		
		action = raw_input("What combo will you do? (Kick Punch, Kick Kick, Punch Punch)> ")
		
		if action == "Kick Punch":
			print "You do the same kick punch combo that you did to the other guy, but the alien expects it. He blocks"
			print "your attack and also pulls out his gun. He shoots you and you die, but you brain is later gotten to study."
			return 'death'
		if action == "Kick Kick":
			print "The translator doesn't even see it comin'! You kick his upper theigh and then you kick his head. He's out cold."
			print "Great work! Now you're off to the Head-Alien's room to get home."
			return 'bossesroom'
		if action == "Punch Punch":
			print "Punch Punch has no effect, sorry but you aren't strong enough. You run after that with the translator cussing you"
			print "out in their language. It's a good thing that you got to do track your freshman year... because you outrun the"
			print "alien and go to the Head-Alien's room to get home."
			return 'bossesroom'
class BossesRoom(Scene):
	def enter(self):
		print "After running around trying to find it, you find the room. You take a deap breath, and then you open the doors with"
		print "an aggressive face on. When you walk in, you find the Head-Alien sitting in his throne of bones, staring at you,"
		print "staring at him. He says words in his language (a translator will translate):"
		print "jdkne uhfuen asdjimn fbhe daj kwni? dneb nuna ijkn huda ombe bud obsh aubf kemi wogh beugh eihm abfud abdia ienjd enid?"
		print "TRANSLATOR: So you want to go home do you? Then are we going to stand here all day, or are we going to fight?"
		print "You haven't even known alien's existed until about 30 minutes ago. What do you do?"
		
		action = raw_input("What will you do? Fight, Cry, Run, or Shoot with an alien's gun?> ")
		
		if action == "Fight":
			print "You try to fight but you thought it was only going to be a fight between the Head-Alien and yourself. You have to"
			print "fight the 5 other aliens in the room... You die in the process of fighting. Sorry."
			return 'death'
		if action == "Cry":
			print "You start breaking down crying in front of him. \"jfnu nejn dfesd...\" which means \'No don't start crying...\'"
			print "The Head-Alien then starts crying and you guys agree to let you go, and you work out your differences with each other."
			return 'afterhome'
		if action == "Run":
			print "The aliens pull out their guns and you start running out the doors you came in. You take a left, then another left, then"
			print "a right, and a middle hall. You get totally lost and the aliens can't find you. You might be there for days, even weeks."
			print "One day you feel a shake like an earthquake, then you hear that we're taking off. Your head explodes due to lack of oxygen"
			print "in space."
			return 'death'
		if action == "Shoot with an alien's gun":
			print "You get a gun from the alien standing next to you, shoot him, and 4 other aliens in the room. Then it's just down to you"
			print "and the boss. You run up to the throne and point the gun to his head. He says \"jfbe ausd daiu jfbe fhue\" which means he"
			print "will take you home."
			return 'afterhome'
class AfterHome(Scene):
	def enter(self):
		print "After being dropped off at your door step, you pull out your keys and open the door, then asking for your mom to come to the"
		print "front room. She said she was watching the news and saw that an alien space ship was here on earth. You give her a look and"
		print "say \"We need to talk...\" After you try explaining to her how heroic you were and how you were almost killed, she asked if "
		print "you were okay, and when you said you were, she gave you a big hug with tears running down her face. \"Great! I love you more"
		print "than you know Jenny Addison. I hate things like that happening.\" You then start to wonder what \'things\'. Then you just"
		print "forget it and move on with your day."
		print "\"I hope this is an excused absence\""
		return 'finished'
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n-------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
class Map(object):
	scenes = {
		'home': Home(),
		'school': School(),
		'spaceship': SpaceShip(),
		'bossesroom': BossesRoom(),
		'afterhome': AfterHome(),
		'death': Death()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('home')
a_game = Engine(a_map)
a_game.play()