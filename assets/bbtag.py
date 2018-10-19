from os import sep

import collections

image_path = "assets/bbtag.png"
coll = collections.OrderedDict([
    ('a', (0, 0, 83, 83)),
    ('b', (85, 0, 83, 83)),
    ('c', (167, 0, 84, 83)),
    ('d', (251, 0, 84, 83)),
    ('p', (336, 0, 83, 83))
])

_inputs = {
    image_path: coll
}
