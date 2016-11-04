#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage


def parse_stix(pkg):
    print("== TTP ==")
    for thing in pkg.ttps:
        print("Title: " + str(thing.title))
        print("Resource: " + str(thing.resources.infrastructure.types[0]))
        for obs in pkg.observables.observables:
            print("Observable: " + str(obs.object_.properties))

    return 0

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
    except:
        exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
