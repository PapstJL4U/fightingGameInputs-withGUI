from os import sep

import collections

image_path = "assets/arcsys_additional.png"
coll = collections.OrderedDict([
    ('j.', (0,0,53,43)),
    ('j', (0,0,53,43)),
    ('jc', (54,0,83,43)),
    ('jc.', (54,0, 83,43)),
    ('djc', ( 136, 0, 120,43)),
    ('djc.', ( 136, 0, 120,43))
])

_inputs = {
    image_path: coll
}
