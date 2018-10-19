from os import sep

import standard_directionals
import complex_directionals
import extra_notations
import guiltygear

_inputs = {}
_inputs.update(standard_directionals._inputs)
_inputs.update(complex_directionals._inputs)
_inputs.update(guiltygear._inputs)
_inputs.update(extra_notations._inputs)