from os import sep

import standard_directionals
import complex_directionals
import extra_notations
import bbtag
import arcsys_additional

_inputs = {}
_inputs.update(standard_directionals._inputs)
_inputs.update(complex_directionals._inputs)
_inputs.update(bbtag._inputs)
_inputs.update(extra_notations._inputs)
_inputs.update(arcsys_additional._inputs)