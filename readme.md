# fightingGameInputs-tti

Text-to-image for fighting game inputs: generate images from fighting game notations.

Thanks to /u/zhx for the icons :)

# Requirements:
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [pygame](http://www.pygame.org/download.shtml)

Installation:

    $ pip install --user -r ./requirements.txt

Installation - with virtualenv:

    $ virtualenv .
    $ source bin/activate
    $ pip install -r ./requirements.txt

# How to use
For full and extensive help, just run: `python inputs-tti.py -h`.

# How to compose the input string
Each input in the string must be separated by a single space. You can get a list of
available commands for a game by typing `python inputs-tti.py -g sf -A`

# Example strings and outputs for Street Figther Type Game
SF5 Ken advanced combo :

`python inputs-tti.py -g sf -i "2 mp , 4 mp > hp qcb mk srk 2p" -c "255 0 0 255"`

Output: http://i.imgur.com/958RNBx.png

---

SF4 Viper bnb into Ultra :

`python inputs-tti.py -g sf -i "hp xx qcb hp ~ 3p , down hp xx srk 2p down upright qcb lk , qcf qcf 3p"`

Output: http://i.imgur.com/RysuscW.png

---

SF4 Ryu solar plexus uppercut FADC to victory :

`python inputs-tti.py -g sf -i "6 hp , 2 mp , 2 hp xx srk lp , mp + mk xx dash , qcf qcf 3p"`

Output: http://i.imgur.com/OMuG2s8.png
