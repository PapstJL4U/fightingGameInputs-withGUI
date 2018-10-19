from os import sep

import collections

image_path = "assets/guiltygear.png"

coll = collections.OrderedDict([
                            ('p', (0, 0, 78, 78)),
                            ('k', (77, 0, 78, 78)),
                            ('s', (154 , 0, 78, 78)),
                            ('hs', (233, 0, 78,78)),
                            ('d', (312, 0, 78, 78))
])

_inputs = {
    image_path: coll
}
