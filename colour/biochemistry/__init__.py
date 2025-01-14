# -*- coding: utf-8 -*-

import sys

from colour.utilities.deprecation import ModuleAPI, build_API_changes
from colour.utilities.documentation import is_documentation_building

from .michaelis_menten import (
    REACTION_RATE_MICHAELISMENTEN_METHODS,
    reaction_rate_MichaelisMenten,
    SUBSTRATE_CONCENTRATION_MICHAELISMENTEN_METHODS,
    substrate_concentration_MichaelisMenten,
)
from .michaelis_menten import (
    reaction_rate_MichaelisMenten_Michaelis1913,
    substrate_concentration_MichaelisMenten_Michaelis1913,
    reaction_rate_MichaelisMenten_Abebe2017,
    substrate_concentration_MichaelisMenten_Abebe2017,
)
__all__ = [
    'REACTION_RATE_MICHAELISMENTEN_METHODS', 'reaction_rate_MichaelisMenten',
    'SUBSTRATE_CONCENTRATION_MICHAELISMENTEN_METHODS',
    'substrate_concentration_MichaelisMenten'
]
__all__ += [
    'reaction_rate_MichaelisMenten_Michaelis1913',
    'substrate_concentration_MichaelisMenten_Michaelis1913',
    'reaction_rate_MichaelisMenten_Abebe2017',
    'substrate_concentration_MichaelisMenten_Abebe2017'
]


# ----------------------------------------------------------------------------#
# ---                API Changes and Deprecation Management                ---#
# ----------------------------------------------------------------------------#
class biochemistry(ModuleAPI):
    def __getattr__(self, attribute):
        return super(biochemistry, self).__getattr__(attribute)


# v0.4.0
API_CHANGES = {
    'ObjectRenamed': [
        [
            'colour.biochemistry.reaction_rate_MichealisMenten',
            'colour.biochemistry.reaction_rate_MichaelisMenten',
        ],
        [
            'colour.biochemistry.substrate_concentration_MichealisMenten',
            'colour.biochemistry.substrate_concentration_MichaelisMenten',
        ],
    ]
}
"""
Defines the *colour.biochemistry* sub-package API changes.

API_CHANGES : dict
"""

if not is_documentation_building():
    sys.modules['colour.biochemistry'] = biochemistry(
        sys.modules['colour.biochemistry'], build_API_changes(API_CHANGES))

    del ModuleAPI, is_documentation_building, build_API_changes, sys
