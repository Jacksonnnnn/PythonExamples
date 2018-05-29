try:
	from setuptools import setuptools
	except ImportError:
		from distutils.core import setup
	
	config = {
		'description': 'My Project',
		'author': 'MyName',
		'url': 'URL to get it at.',
		'download_url': 'Where to download it.',
		'author_email': 'My Email',
		'version': '0.1',
		'install_requires': ['nose']
		'packages': ['NAME']
		'scripts': [],
		'name': 'projectname'
}
def test_room():
	gold = Room("GoldRoom",
				"""This room has gold in it you can grab. there's a door to the north."""
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Roon("Dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
setup(**config)