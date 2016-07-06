import sys, os, re
import pygame
from StringIO import StringIO

path = 'assets' + os.sep

_input = {
		'lpmp': path + 'lpmp.png',
		'lphp': path + 'lphp.png',
		'mphp': path + 'mphp.png',
		'lkmk': path + 'lkmk.png',
		'lkhk': path + 'lkhk.png',
		'mkhk': path + 'mkhk.png',
		'2k': path + '2k.png',
		'2p': path + '2p.png',
		'3k': path + '3k.png',
		'3p': path + '3p.png',
		'chargeback': path + 'chargeback.png',
		'chargedown': path + 'chargedown.png',
		'comma': path + 'comma.png',
		'd': path + 'd.png',
		'dash': path + 'dash.png',
		'down': path + 'down.png',
		'downleft': path + 'downleft.png',
		'downright': path + 'downright.png',
		'greaterthan': path + 'greaterthan.png',
		'hcb': path + 'hcb.png',
		'hcf': path + 'hcf.png',
		'hk': path + 'hk.png',
		'hp': path + 'hp.png',
		'hs': path + 'hs.png',
		'k': path + 'k.png',
		'left': path + 'left.png',
		'lk': path + 'lk.png',
		'lp': path + 'lp.png',
		'mk': path + 'mk.png',
		'mp': path + 'mp.png',
		'neutral': path + 'neutral.png',
		'p': path + 'p.png',
		'plus': path + 'plus.png',
		'qcb': path + 'qcb.png',
		'qcf': path + 'qcf.png',
		'right': path + 'right.png',
		'rsrk': path + 'rsrk.png',
		's': path + 's.png',
		'spd': path + 'spd.png',
		'srk': path + 'srk.png',
		'tilde': path + 'tilde.png',
		'up': path + 'up.png',
		'upleft': path + 'upleft.png',
		'upright': path + 'upright.png',
		'xx': path + 'xx.png',
}

_width = {
		'lpmp': 120,
		'lphp': 120,
		'mphp': 120,
		'lkmk': 120,
		'lkhk': 120,
		'mkhk': 120,
		'2k': 120,
		'2p': 120,
		'3k': 120,
		'3p': 120,
		'chargeback': 83,
		'chargedown': 50,
		'comma': 30,
		'd': 84,
		'dash': 76,
		'down': 52,
		'downleft': 60,
		'downright': 60,
		'greaterthan': 41,
		'hcb': 93,
		'hcf': 92,
		'hk': 86,
		'hp': 84,
		'hs': 82,
		'k': 85,
		'left': 72,
		'lk': 85,
		'lp': 84,
		'mk': 84,
		'mp': 84,
		'neutral': 56,
		'p': 86,
		'plus': 44,
		'qcb': 74,
		'qcf': 75,
		'right': 72,
		'rsrk': 65,
		's': 84,
		'spd': 85,
		'srk': 64,
		'tilde': 44,
		'up': 50,
		'upleft': 60,
		'upright': 68,
		'xx': 71,
}

def usage():
	print "Usage:"
	print "$ python inputs-tti.py \"string\" [\"R G B A\"]"
	print "For the input string format, check out the examples or the source code."
	print "The RGBA string should be formatted like that : \"255 122 122 255\", and allows you to fill the background."
	print "Example:"
	print "$ python inputs-tti.py \"D MP , D MP XX DP 2P\""
	print "Image saved to result.png!"

if __name__ == '__main__':
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		usage()
		sys.exit(1)

	if len(sys.argv) == 3:
		colorarg = sys.argv[2].split(' ')
		_color = pygame.Color(int(colorarg[0]), int(colorarg[1]), int(colorarg[2]), int(colorarg[3]))

	_string = sys.argv[1]
	_string = _string.lower()

	robj = re.compile(r'\b(' + '|'.join(_input.keys()) + r')\b')
	_result = robj.sub(lambda m : _input[m.group(0)], _string)

	# Arrange inputs
	_result = _result.split(' ')
	for i in range(len(_result)):
		if _result[i] == ',':
			_result[i] = path + 'comma.png'
		elif _result[i] == '+':
			_result[i] = path + 'plus.png'
		elif _result[i] == '~':
			_result[i] = path + 'tilde.png'
		elif _result[i] == '>':
			_result[i] = path + 'greaterthan.png'
		elif _result[i] == '1':
			_result[i] = path + 'downleft.png'
		elif _result[i] == '2':
			_result[i] = path + 'down.png'
		elif _result[i] == '3':
			_result[i] = path + 'downright.png'
		elif _result[i] == '4':
			_result[i] = path + 'left.png'
		elif _result[i] == '5':
			_result[i] = path + 'neutral.png'
		elif _result[i] == '6':
			_result[i] = path + 'right.png'
		elif _result[i] == '7':
			_result[i] = path + 'upleft.png'
		elif _result[i] == '8':
			_result[i] = path + 'up.png'
		elif _result[i] == '9':
			_result[i] = path + 'upright.png'

	_images = []
	totalwidth = 0
	for i in range(len(_result)):
		_images.append(pygame.image.load(_result[i]))
		totalwidth += _width[_result[i][7:-4]]
	dimensions = (totalwidth, 120)
	_surface = pygame.Surface(dimensions, pygame.SRCALPHA, 32)
	if len(sys.argv) == 3:
		pygame.draw.rect(_surface, _color, (0, 0, totalwidth, 120), 0)
	totalwidth = 0
	for i in range(len(_images)):
		_surface.blit(_images[i], (totalwidth, 0))
		totalwidth += _width[_result[i][7:-4]]
	pygame.image.save(_surface, "result.png")

	print "Image saved to result.png!"