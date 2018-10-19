from os import sep

import collections

image_path = "assets/guiltygear_modern.png"

coll = collections.OrderedDict([
                            ('p', (0, 0, 72, 72)),
                            ('k', (73, 0, 72, 72)),
                            ('s', (144 , 0, 72, 72)),
                            ('hs', (216, 0, 72, 72)),
                            ('d', (287, 0, 72, 72))
])

_inputs = {
    image_path: coll
}
