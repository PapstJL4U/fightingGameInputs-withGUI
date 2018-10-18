from os import sep

import collections

image_path = "assets/extra_notations.png"
coll = collections.OrderedDict([
                        ('>', (0,0,33,51)),
                        ('xx', (33,0,69,50)),
                        (',', (139,0,16,50)),
                        ('~', (101,0,36,18)),
                        ('+', (101,19,36,36))
])

_inputs = {
    image_path: coll
}
