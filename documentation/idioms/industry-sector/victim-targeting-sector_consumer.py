#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage

def parse_stix( pkg ):
    print("== TTP ==")
    for thing in pkg.ttps:
        print("---")
        print("TTP: " + thing.title)
        print("Victim: " + str(thing.victim_targeting.identity.specification.organisation_info.industry_type))

    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
