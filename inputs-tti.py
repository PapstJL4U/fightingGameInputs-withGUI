#!/usr/bin/python

import sys, os, re, argparse, string
import pygame

sys.path.append('games')
sys.path.append('assets')

# Create and configure arguments parser
parser = argparse.ArgumentParser(description="Text-to-image for fighting game inputs")
group = parser.add_mutually_exclusive_group()
group.add_argument("-g", "--game", help="standard template for a specific game.\
        Default is dbfz", default = "dbfz")
group.add_argument("-t", "--template", help="import custom image template.\
        For an example template look at the standard games.")

group2 = parser.add_mutually_exclusive_group(required=True)
group2.add_argument("-A", "--available-inputs", help="display available inputs and exit",
        action="store_const", const=True)
group2.add_argument("-i", "--input", help="input string. \
        Complete list of available inputs can be displayed with option '-H'.")
group2.add_argument("-l", "--list-games", help="list avaialable games", action="store_const", const=True)

parser.add_argument("-o", "--output", help="name of the produced file, in the output/ folder. \
        If not given, a name will be created based on the input string.")
parser.add_argument("-c", "--color", help="color of the background. Syntax is \"R G B A\", \
        values must be between 0 and 255. Default is clear", default = "0 0 0 0")
parser.add_argument("-p", "--padding", help="padding in between each input.", default = "10")
args = vars(parser.parse_args());

if __name__ == '__main__':

    if args["list_games"] is not None:
        #dynamically get .py files in games/ and list them here
        print "Found:\ndbfz\nsf"
        sys.exit(0)

# check for game / template
    # this most definitely needs more error checking
    if args["template"] is not None:
        m = __import__(args["template"])
    elif args["game"] is not None:
        m = __import__(args["game"])

    #import inputs from selected game
    inputs = {}
    inputs.update(m._inputs)

    if args["available_inputs"] is not None:
        for image in inputs:
            print image
            for key in inputs[image]:
                if key == inputs[image].keys()[-1]:
                    print key
                else:
                    sys.stdout.write(key + ", ")
        sys.exit(0)

    # argparse arguments
    inputString = args["input"]
    outputFile = args["output"] if args["output"] != None else inputString
    outputFile = ''.join(c for c in outputFile
            if c in "-_.() %s%s" % (string.ascii_letters, string.digits))\
            .replace(" ", "")

    color = args["color"] if args["color"] != None else "0 0 0 0"
    colorarg = color.split(' ')
    _color = pygame.Color(int(colorarg[0]), int(colorarg[1]), int(colorarg[2]), int(colorarg[3]))

    _string = inputString.lower()

    padding = int(args["padding"])

    _positions = []
    _image_list = []
    _images = {}
    totalWidth = 0
    highestHeight = 0

    #probably could use some optimization
    # checks each command for the first occurance in any dictionary
    #   saves off data for that command before moving on
    for com in _string.split(' '):
        for image in inputs:
            if com in inputs[image].keys():
                # Should do more for complext paths...
                path = image.split('/')
                _images.update({image:pygame.image.load(os.path.join(path[0],path[1]))})
                _image_list += [image]
                _positions += [pygame.Rect(inputs[image][com])]
                totalWidth += pygame.Rect(inputs[image][com]).width + padding
                if highestHeight < pygame.Rect(inputs[image][com]).height:
                    highestHeight = pygame.Rect(inputs[image][com]).height
                break

    _surface = pygame.Surface((totalWidth, highestHeight), pygame.SRCALPHA, 32)
    pygame.draw.rect(_surface, _color, (0, 0, totalWidth, highestHeight), 0)

    pos = 0

    for i in range(len(_image_list)):
        _surface.blit(_images[_image_list[i]], (pos,(highestHeight-_positions[i].height)/2), _positions[i])
        pos += _positions[i].width + padding

    pygame.image.save(_surface, os.path.join("output", outputFile + ".png"))
    print "Image saved to " + os.path.join("output", outputFile + ".png") + " !"
