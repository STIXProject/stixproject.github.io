#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    print "== ACTOR =="
    for actor in pkg.threat_actors:
        print "Actor: " + actor.title
        for name in actor.identity.specification.party_name.organisation_names:
            print "AKA: "+ str(name.name_elements[0].value)
        print "Language: " + actor.identity.specification.languages[0].value
        print "Country: " + str(actor.identity.specification.addresses[0].country.name_elements[0].value)
        print "Area: " + str(actor.identity.specification.addresses[0].administrative_area.name_elements[0].value)
        
        for addr in actor.identity.specification.electronic_address_identifiers:
            print "Internet Address: " + str(addr.value)
    
    
    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
