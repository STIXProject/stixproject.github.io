#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    kill_chains = {}
    kill_chain_phases = {}
    print "== TTP =="
    for chain in pkg.ttps.kill_chains:
        kill_chains[chain.id_] = chain.name
        print "--"
        print "Name: " + chain.name
        print "Definer: " + chain.definer
        
        for phase in chain.kill_chain_phases: 
            kill_chain_phases[phase.phase_id] = str(phase.name)
            print "Phase: " + str(phase.name)

    print "== Indicator =="
    for indicator in pkg.indicators:
        print "ID: " + indicator.id_
        for phase in indicator.kill_chain_phases:
            print "  == Kill Chain Reference =="
            print "  Name: " + kill_chains[phase.kill_chain_id]
            print "  Phase: " + kill_chain_phases[phase.phase_id]
        
    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
