#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    print "== TTP =="
    for chain in pkg.ttps.kill_chains:
        print "--"
        print "Name: " + chain.name
        print "Definer: " + chain.definer
        
        for phase in chain.kill_chain_phases: 
            print "Phase: " + str(phase.name)
        
    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
