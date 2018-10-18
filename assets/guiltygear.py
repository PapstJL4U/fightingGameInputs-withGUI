from os import sep

import collections

image_path = "assets/guiltygear.png"
coll = collections.OrderedDict([
                            ('p', (0, 0, 78, 78)),
                            ('k', (78, 0, 154, 78)),
                            ('s', (154 , 0, 233, 78)),
                            ('hs', (233, 0, 312,78)),
                            ('d', (312, 0, 78, 78))
])

_inputs = {
    image_path: coll
}
