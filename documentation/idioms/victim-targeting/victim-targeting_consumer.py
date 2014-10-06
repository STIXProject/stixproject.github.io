#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    ttp_list = {}
    for tactic in pkg.ttps:
        ttp_list[tactic.id_] = tactic
    
    
    print "== Campaign =="
    for camp in pkg.campaigns:
        print "---"
        print "Campaign: " + str(camp.title)
        
        for tactic in camp.related_ttps:
            print "RelatedTTP: " + ttp_list[tactic.item.idref].title
            print "Relationship: " + str(tactic.relationship)
            for target in ttp_list[tactic.item.idref].victim_targeting.targeted_information:
                print "Target: " + str(target)
    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
