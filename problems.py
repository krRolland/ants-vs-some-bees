import ants, importlib


def print_armor(beelist):
	returnList = []
	for b in beelist: 
		temparmor = bee.armor
		returnList += temparmor 
	return returnList

def print_bees(p): 
	assert type(p) == ants.Place, "not passing a place"
	while p.exit !=None:
		p = p.exit
	while p.entrance !=None:
		print(print_armor(p.bees))
		p = p.entrance
	return