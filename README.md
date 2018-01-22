# fightingGameInputs-tti

Text-to-image for fightning game inputs : generate images from fighting game notations.

HUGE thanks to /u/zhx for the sexiest icons. :)

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
`python inputs-tti.py "string" ["R G B A"]`

For the input string format, see below.

R, G, B, and A are values between 0 and 255. These are optional.

The default background will be transparent.

# How to compose the input string
Each input in the string must be separated by a single space.

Recognized commands:
* Punches : p, 2p, 3p, lp, mp, hp
* Kicks : k, 2k, 3k, lk, mk, hk
* Specific 2-input combinations : lpmp, lphp, mphp, lkmk, lkhk, mkhk
* Guilty Gear extras : p, k, s, h, d
* Directions : downleft (1), down (2), downright (3), left (4), neutral (5), right (6), upleft (7), up (8), upright (9)
* Charges : chargeback, chargedown
* Motions : qcb, qcf, hcb, hcf, dash, srk, rsrk, spd
* Link/chain notations : comma (,), greaterthan (>), plus (+), tilde (~), xx.

# Example strings and outputs
SF5 Ken advanced combo :

`python inputs-tti.py "2 mp , 4 mp > hp qcb mk srk 2p" "255 0 0 255"`

Output: http://i.imgur.com/958RNBx.png

---

SF4 Viper bnb into Ultra :

`python inputs-tti.py "hp xx qcb hp ~ 3p , down hp xx srk 2p down upright qcb lk , qcf qcf 3p"`

Output: http://i.imgur.com/RysuscW.png

---

SF4 Ryu solar plexus uppercut FADC to victory :

`python inputs-tti.py "6 hp , 2 mp , 2 hp xx srk lp , mp + mk xx dash , qcf qcf 3p"`

Output: http://i.imgur.com/OMuG2s8.png
