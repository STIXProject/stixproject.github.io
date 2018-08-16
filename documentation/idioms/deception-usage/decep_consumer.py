#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    print "== INCIDENT =="
    for inc in pkg.incidents:
        for coa in inc.coa_requested:
          requested = coa.course_of_action
          print "COA: " + str(requested.title)
          print "Stage: "+ str(requested.stage)
          print "Type: "+ str(requested.type_)
          print "Objective: "+ str(requested.objective.description)
          
    return

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
