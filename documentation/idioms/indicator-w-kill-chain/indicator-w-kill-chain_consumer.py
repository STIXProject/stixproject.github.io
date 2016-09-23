#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    
    # load kill chains
    phases = {}
    for chain in pkg.ttps.kill_chains:
        for phase in chain.kill_chain_phases: 
            phases [phase.phase_id] = phase.name
    
    
    print("== INDICATOR ==")
    for ind in pkg.indicators:
        print("--")
        print("Title: " + ind.title)
        print("Description: " + str(ind.description))
        for phase in ind.kill_chain_phases:
            # lookup phase by ID
            print("Kill Chain Phase: " + str(phases[phase.phase_id]))
        
    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
