#!/usr/bin/python

import sys, os, re, argparse, string
import pygame

from constants import _available, _input, _width, path
# Create and configure arguments parser
parser = argparse.ArgumentParser(description="Text-to-image for fighting game inputs")
parser.add_argument("-O", "--correct-options", help="display available inputs and exit",
        action="store_const", const=True)
parser.add_argument("-i", "--input", help="input string. \
        Complete list of available inputs can be displayed with option '-H'.", required=True)
parser.add_argument("-o", "--output", help="name of the produced file, in the output/ folder. \
        If not given, a name will be created based on the input string.")
parser.add_argument("-c", "--color", help="color of the background. Syntax is \"R G B A\", \
        values must be between 0 and 255.")
args = vars(parser.parse_args())

def parseCombo(inputString, outputFile, color):

    colorarg = color.split(' ')
    _color = pygame.Color(int(colorarg[0]), int(colorarg[1]), int(colorarg[2]), int(colorarg[3]))
    _string = inputString.lower()

    robj = re.compile(r'\b(' + '|'.join(_input.keys()) + r')\b')
    _result = robj.sub(lambda m: _input[m.group(0)], _string)

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
        try:
            _images.append(pygame.image.load(_result[i]))
        except pygame.error as err:
            print("No image for "+_result[i]+".")
            i = pygame.image.load("assets"+os.sep+"invalidcombo.png")
            pygame.image.save(i, os.path.join("output", outputFile + ".png"))
            return
        totalwidth += _width[_result[i][7:-4]]
    dimensions = (totalwidth, 120)
    _surface = pygame.Surface(dimensions, pygame.SRCALPHA, 32)
    pygame.draw.rect(_surface, _color, (0, 0, totalwidth, 120), 0)
    totalwidth = 0
    for i in range(len(_images)):
        _surface.blit(_images[i], (totalwidth, 0))
        totalwidth += _width[_result[i][7:-4]]

    pygame.image.save(_surface, os.path.join("output", outputFile + ".png"))


if __name__ == '__main__':
    if args["correct_options"] is not None:
        print("List of available inputs:\n" + _available)
        sys.exit(0)

    # argparse arguments
    inputString = args["input"]
    outputFile = args["output"] if args["output"] != None else inputString
    outputFile = ''.join(c for c in outputFile
                         if c in "-_.() %s%s" % (string.ascii_letters, string.digits)) \
        .replace(" ", "")
    color = args["color"] if args["color"] != None else "0 0 0 0"

    parseCombo(inputString, outputFile, color)
    print("Image saved to " + os.path.join("output", outputFile + ".png") + " !")