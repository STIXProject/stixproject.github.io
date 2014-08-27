#!/usr/bin/env python

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    print "== INDICATOR =="
    print "Package: " + str(pkg.stix_header.description)
    print "Submitter: " + pkg.stix_header.information_source.identity.name
    for inc in pkg.incidents:
        print "---"
        print "Incident: "+ inc.title
        print "Description: "+ str(inc.description)
        print "Confidence: "+ str(inc.confidence.value)
        for impact in inc.impact_assessment.effects:
            print "Impact: "+ str(impact)
        print "Initial Compromise: "+ str(inc.time.initial_compromise.value)
        print "Incident Discovery: "+ str(inc.time.incident_discovery.value)
        print "Restoration Achieved: "+ str(inc.time.restoration_achieved.value)
        print "Incident Reported: "+ str(inc.time.incident_reported.value)

        for victim in inc.victims:
            print "Victim: "+ str(victim.name)

    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
