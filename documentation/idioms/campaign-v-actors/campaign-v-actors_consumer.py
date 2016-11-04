#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage


def parse_stix(pkg):

    for camp in pkg.campaigns:
        print("== CAMPAIGN ==")
        print("Campaign Name: " + str(camp.title))

        for tactic in camp.related_ttps:
            print("TTP: " + tactic.item.title)

        for attrib in camp.attribution:
            print("Actor: " + attrib[0].item.title)

        for rel in camp.related_incidents:
            print("Related Incident ID: " + str(rel.item.idref))

    return 0

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
    except:
        exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
