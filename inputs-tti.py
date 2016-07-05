import sys, os, re
import pygame
from StringIO import StringIO

path = 'assets' + os.sep

_input = {
	'P': path + 'p' + '.pngZ',
	'LP': path + 'lp' + '.pngZ',
	'MP': path + 'mp' + '.pngZ',
	'HP': path + 'hp' + '.pngZ',
	'3P': path + '3p' + '.pngZ',
	'K': path + 'k' + '.pngZ',
	'LK': path + 'lk' + '.pngZ',
	'MK': path + 'mk' + '.pngZ',
	'HK': path + 'hk' + '.pngZ',
	'3K': path + '3k' + '.pngZ',
	'DB': path + '1' + '.pngZ',
	'D': path + '2' + '.pngZ',
	'DF': path + '3' + '.pngZ',
	'B': path + '4' + '.pngZ',
	#'N': path + '5' + '.pngZ',
	'F': path + '6' + '.pngZ',
	'FF': path + '66' + '.pngZ',
	'UB': path + '7' + '.pngZ',
	'U': path + '8' + '.pngZ',
	'UF': path + '9' + '.pngZ',
	'QCF': path + 'qcf' + '.pngZ',
	'QCB': path + 'qcb' + '.pngZ',
	'HCF': path + 'hcf' + '.pngZ',
	'HCB': path + 'hcb' + '.pngZ',
	'SPD': path + 'spd' + '.pngZ',
	'DP': path + 'srk' + '.pngZ',
	'RDP': path + 'rsrk' + '.pngZ',
	'and': path + 'and' + '.pngZ',
}

def usage():
	print "Usage:"
	print "$ python inputs-tti.py \"string\""
	print "Example:"
	print "$ python inputs-tti.py \"DMPDMPQCFHP\""
	print "Image saved to result.png!"

if __name__ == '__main__':
	if len(sys.argv) != 2:
		usage()
		sys.exit(1)

	_string = sys.argv[1]
	#_string = _string.upper()

	robj = re.compile('|'.join(_input.keys()))
	_result = robj.sub(lambda m : _input[m.group(0)], _string)
	_result = _result.split('Z')[:-1]
	_images = []
	for i in _result:
		_images.append(pygame.image.load(i))
	dimensions = (110 * len(_images) + 20, 120)
	_surface = pygame.Surface(dimensions)
	_surface.fill((0, 255, 0))
	for i in range(len(_images)):
		_surface.blit(_images[i], (-10 + 110 * i, 0))
	pygame.image.save(_surface, "result.png")