import sys, os, re
import pygame

from constants import _input, _width, path

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
